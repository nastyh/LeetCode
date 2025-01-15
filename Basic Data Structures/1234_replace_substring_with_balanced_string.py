from typing import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        """
        O(n) to traverse
        O(1) since it's a dict of 26 keys
        Sliding window
        Each char should have a target frequency
        Calculate how many times each character exceeds the target frequency
        Use a sliding window to find the smallest substring where replacing it would balance the string
        Start with both l and r pointers at the beginning of the string.
        Expand the right pointer to include characters, and shrink the left pointer
        to check if the substring can balance the string.
        While the substring represented by the sliding window balances the string
        (i.e., the rest of the string can be balanced), shrink the window.
        """
        d = Counter(s)
        n, target = len(s), len(s) // 4
        l, min_length = 0, n
        # best case
        if all(v == len(s) / 4 for v in d.values()):
            return 0
        excess = {char: max(0, d[char] - target) for char in "QWER"}
        for r in range(n):
            d[s[r]] -= 1

            while all(d[char] <= target for char in "QWER"):
            # Update the minimum length
                min_length = min(min_length, r - l + 1)
                
                # Shrink the window from the left
                d[s[l]] += 1
                l += 1
        
        return min_length

        