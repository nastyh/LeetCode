class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        O(nlogn) and O(1)
        After sorting the array, we perform a binary search to find the kth smallest distance.
        The binary search is conducted on the range of possible distances between elements in the array.
        We initialize left to 0 (minimum possible distance) and right to the maximum possible difference
        between any two elements in the sorted array (nums[-1] - nums[0]).
        In each iteration of the binary search, we calculate the midpoint mid between left and right.
        We then use the helper function to count the number of pairs with distances less than or equal to mid.
        This function performs a linear scan through the array and counts such pairs.
        If the count is less than k, we know that the kth smallest distance must be larger than mid, so we update left to mid + 1.
        If the count is greater than or equal to k, we update right to mid because we need to find a smaller distance.
        The binary search continues until left is no longer less than right, at which point left will be equal to the kth smallest distance.
        The helperfunction performs a linear scan through the sorted array to count the number
        of pairs with distances less than or equal to mid. This count is achieved by maintaining two pointers,
        left and right, which point to the start and end of the sliding window of elements.
        We start with left at index 0 and iterate through the array with right increasing from 0 to the end of the array.
        While the difference between nums[right] and nums[left] is greater than mid, we increment left to shrink the window.
        For each right, the number of valid pairs with distances less than or equal to mid is the difference between right
        and left. This is because the array is sorted, and as long as the difference condition is met, all elements between left and right are valid pairs.
        The function returns the total count of such pairs.
        """
        def _helper(nums, mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = _helper(nums, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def smallestDistancePair_another(self, nums: List[int], k: int) -> int:
        """
        O(nlog(n) + nlog(max pair distance) + n)
        O(1)
        """
        nums.sort()
        def _helper(guess):
            left = count = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k
        
        low, high = 0, nums[-1] - nums[0]
        while low <= high:
            mid = (low + high) // 2
            
            if _helper(mid):
                high = mid - 1
            else:
                low = mid + 1
        return high + 1