class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        O(nlogn) and O(1)
        if target < nums[m], target is smaller than everything to the right of m
        if target > nums[m], target is larger than everything to the left of m 

        Case 1: nums[m] >= nums[l]. Left is sorted from here 
          nums[l] >= target and target < nums[m] --> process the left half
          else: move to the right side
        Case 2: nums[m] < nums[l]. Left is rotated, right is sorted. 
          if nums[m] < target and target < nums[r] --> right contains target, move there
          else: move to the left side
        """
        l, r = 0, len(nums) - 1
        while l <= r: 
            m = l + (r - l) // 2
            # ideal solution
            if nums[m] == target:
                return m 
            # the left portion from m is sorted
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 
            