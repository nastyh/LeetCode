from typing import Counter, List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        O(n) both 
        freq to find which element appears more than half the time in nums. 
        It's the problem statement
        Loop till the second last and update left_count for occurrences of the dominant element in the left subarray.
        for the left subarray of len i+1, the dominant el must occur more than (i+1)/2 times
        for the right subarray, n - i - 1, the count of the dominant element (overall_count - left_count) must 
        be more than (n-i-1)/2
        As soon as both are met, the curr index is the smalles valid split, return
        """
        n = len(nums)
        # Step 1: Identify the overall dominant element.
        freq = Counter(nums)
        majority = None
        overall_count = 0
        for num, count in freq.items():
            if count > n / 2:
                majority = num
                overall_count = count
                break

        # Step 2: Iterate over possible split points (0 <= i < n - 1)
        left_count = 0
        for i in range(n - 1):
            if nums[i] == majority:
                left_count += 1

            # Left subarray length is i + 1; right subarray length is n - i - 1.
            # Check if majority element is dominant in both subarrays.
            if left_count > (i + 1) / 2 and (overall_count - left_count) > (n - i - 1) / 2:
                return i

        return -1