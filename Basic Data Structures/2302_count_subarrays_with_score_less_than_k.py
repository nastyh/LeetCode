class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        O(n)
        O(1)
        sliding window approach: maintain a window an adjust to 
        make sure its size is under k
        current_sum: sum of elements in a current window
        left: start of the window
        res is the number of valid subarrays 
        """
        current_sum = 0
        left = 0
        res = 0
        for right in range(len(nums)):
            # iterate and add each element to current_sum
            current_sum += nums[right]
            # while the condition is true
            while current_sum * (right - left + 1) >= k:
                # remove the left side of the window
                current_sum -= nums[left]
                left += 1
            res += (right - left + 1) # valid subarrays
        return res