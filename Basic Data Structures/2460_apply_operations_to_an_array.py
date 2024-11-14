class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        """
        O(n) and O(1)
        two steps
        first is to compare and increment
        Second is to move all the zeroes to the left
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums