class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        O(n^2) because of the two for loops
        O(n) because of dp 
        create dp of the same length filled with ones (since one element on its own is an increasing subsequence)
        have two pointers, l and r. Left start from the beginning, right starts from the second element (index 1)
        We move both to the right. For each right pointer we run the left from the beginning of the string up to the
        right pointer.
        If we notice that the element at the right pointer is > the element at the left pointer, we will go to dp
        and update dp[right] as max(dp[right], dp[left] + 1). The second part means that to the left there is a smaller
        number and we continue building the subsequence.
        The subsequence means that the numbers don't have to stand next to each other, it can be
        [43,  2, 100] and the subsequence of [43, 100] will count 
        This is why we run the left pointer from the beginning of the list to the right pointer all the time 
        """
        dp = [1] * len(nums)
        for r in range(1, len(nums)):
            for l in range(r):
                if nums[r] > nums[l]:
                    dp[r] = max(dp[r], dp[l] + 1)
        return max(dp)

    def lengthOfLIS_from_the_back(self, nums: List[int]) -> int:
        """
        same as above but in an opposite order
        i is the left index, j is the right index 
        but here for each left index we check everything to the right 
        numbers to the right should be larger 
        """
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
