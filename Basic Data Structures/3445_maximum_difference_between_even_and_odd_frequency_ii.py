from collections import defaultdict
import math


class Solution:
    def maxDifference_optimal(self, s: str, k: int) -> int:
        """
        O(n), outer loop is 5*5=25 pairs (chars from 0 to 4)
        Inner loop: for each pair, a single pass O(n)
        So O(25*n) = O(n)
        Space is O(1)
        just best of size 4 

        Tracks prefix differences cnt_a - cnt_b as it slides over the string
        Groups those prefixes by parity status of the character counts
        Uses parity XOR tricks to know when two subarrays differ in odd/even status in a way that satisfies the problem
        """
        def getStatus(cnt_a: int, cnt_b: int) -> int:
            """
            encodes the parity (odd/even) of cnt_a and cnt_b as a 2-bit number:
            First bit: whether cnt_a is odd → (cnt_a & 1)
            Second bit: whether cnt_b is odd → (cnt_b & 1)
            Shift the bit for a and combine both into an integer from 0 to 3.
            """
            return ((cnt_a & 1) << 1) | (cnt_b & 1)

        n = len(s)
        ans = -math.inf
        for a in ["0", "1", "2", "3", "4"]:
            for b in ["0", "1", "2", "3", "4"]:
                if a == b:
                    continue

                best = [math.inf] * 4
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b
                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(
                            best[left_status], prev_a - prev_b
                        )
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b

                    right_status = getStatus(cnt_a, cnt_b)
                    #  the ^ sign flips the parity bit of cnt_a, while leaving cnt_b unchanged.
                    if best[right_status ^ 0b10] != math.inf: # 0b10: a binary literal (i.e., the number 2 in decimal), which has only the bit corresponding to cnt_a set
                        ans = max(
                            ans, cnt_a - cnt_b - best[right_status ^ 0b10]
                        )

        return ans

    def maxDifference(self, s: str, k: int) -> int:
        """
        Times out 
        O(n) for a sliding window
        O(1) for five digits 
        """
        n = len(s)
        max_diff = -math.inf
        digits = ['0', '1', '2', '3', '4']
        
        for window_size in range(k, n + 1):
            freq = defaultdict(int)

            # Initialize first window
            for i in range(window_size):
                freq[s[i]] += 1

            def update_max():
                nonlocal max_diff
                for a in digits:
                    if freq[a] % 2 != 1:
                        continue
                    for b in digits:
                        if a == b or freq[b] == 0:
                            continue
                        if freq[b] % 2 == 0:
                            max_diff = max(max_diff, freq[a] - freq[b])

            update_max()

            # Slide window
            for i in range(window_size, n):
                out_char = s[i - window_size]
                in_char = s[i]

                freq[out_char] -= 1
                if freq[out_char] == 0:
                    del freq[out_char]
                freq[in_char] += 1

                update_max()

        return max_diff if max_diff != -math.inf else -1