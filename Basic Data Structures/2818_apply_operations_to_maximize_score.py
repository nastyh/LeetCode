from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        O(n *  sqrt(M) + nlogn) , n array size, M max value of an array
        O(n) extra space for sorting, arrays for prime scores, left and right boundaries

        Using a monotonic stack, we compute for each index the furthest it can “stretch”
        left and right before encountering a blocking element (based on the prime score and tie–break rule).
        After computing how many subarrays (frequency) yield each element as the “winner,”
        we sort by value and use each candidate as many times as allowed (up to its frequency) until we have done k operations. 
        The final score is the product modulo 10**9 + 7  
        """
        mod = 10**9 + 7  
        def _helper_prime_count(x): 
            """
            counts distinct prime factors.
            """
            cnt = 0
        # Check factor 2
            if x % 2 == 0:
                cnt += 1
                while x % 2 == 0:
                    x //= 2
            # Check odd factors up to sqrt(x)
            f = 3
            while f * f <= x:
                if x % f == 0:
                    cnt += 1
                    while x % f == 0:
                        x //= f
                f += 2
            if x > 1:
                cnt += 1
            return cnt
    
        n = len(nums)
        pscore = [_helper_prime_count(x) for x in nums]
        # Compute left and right boundaries for each element.
        left = [-1] * n
        right = [n] * n
        
        # For left, we need previous index with pscore >= current.
        stack = []
        for i in range(n):
            while stack and pscore[stack[-1]] < pscore[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # For right, we need next index with pscore > current.
        stack = []
        for i in range(n-1, -1, -1):
            while stack and pscore[stack[-1]] <= pscore[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Frequency: number of subarrays where nums[i] is chosen.
        freq = [(i - left[i]) * (right[i] - i) for i in range(n)]
        
        # Pair each number with its frequency.
        pairs = [(nums[i], freq[i]) for i in range(n)]
        # Sort in descending order of value.
        pairs.sort(key=lambda x: x[0], reverse=True)
        
        # Greedily pick the highest value multiplications.
        score = 1
        remaining = k
        for val, cnt in pairs:
            if remaining == 0:
                break
            use = min(cnt, remaining)
            # Multiply score by val^use mod MOD.
            score = (score * pow(val, use, mod)) % mod
            remaining -= use
        
        return score
