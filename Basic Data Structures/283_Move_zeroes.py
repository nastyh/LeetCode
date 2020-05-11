class Solution:
    def moveZeroes(self, nums: List[int]) -> None:


        for num in nums:
            if num == 0:
                ix = nums.index(num)
                nums.append(num)
                del nums[ix]
        return nums

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0                   # start from 0 (forward pointer)
        j = len(nums) - 1       # start from end (backward pointer)
        while(i<j):
            if nums[i] ==0:
                nums.pop(i)
                nums.insert(j, 0)
                j -= 1
            else:
                i += 1
        return nums
