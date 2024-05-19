class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # doesn't count since they want in nlogn time
        return nums.index(max(nums))

    def findPeakElement_binary_search(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # usual binary
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]: # potentially a candidate
                r = m # let's keep it in consideration
            else:
                l = m + 1 # # it's a small number, let's look at the right half 
        return l # answer boils down to the left element 