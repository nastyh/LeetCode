from typing import List


class Solution:
    def countBadPairs_optimal(self, nums: List[int]) -> int:
        """
        O(n) to run 
        O(n) for the dict
        question is j - i = nums[j] - nums[i]
        rewrite as nums[i] - i != nums[j] - j 
        or 
        j - nums[j] != i - nums[i]
        key = i-nums[i]
        Dict to count the number of occurences of the i - nums[i]
        for each new j count how many indices i < j form a good pair (where i-nums[i] == j-nums[j])
        All possible pairs minus good pairs == bad pairs 
        """
        n, good_pairs, d = len(nums), 0, {}
        for j in range(n):
            key = j - nums[j]
            if key in d:
                good_pairs += d[key]
            d[key] = d.get(key, 0) + 1

        # total number of pairs we can get from n numbers
        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs

    def countBadPairs_brute_force(self, nums: List[int]) -> int:
        """
        O(N^2) -- two loops
        O(1) -- nothing to store
        Brute force, times out
        Left pointer, right pointer is always starts to the right from the left
        Just process everything and build the result
        """
        # i, j = 0, 1
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if j - i != nums[j] - nums[i]:
                    res += 1
        return res