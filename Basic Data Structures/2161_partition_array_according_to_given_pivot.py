from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        O(n) both
        Simulate, three ifs, return all
        Doesn't necessarily makes everything ordered but still passes
        """
        less, equal, more = [] , [], []
        for ix in range(len(nums)):
            if nums[ix] < pivot:
                less.append(nums[ix])
            elif nums[ix] == pivot:
                equal.append(nums[ix])
            else:
                more.append(nums[ix])
        return less + equal + more
    
    def pivotArray_two_pointers(self, nums: List[int], pivot: int) -> List[int]:
        """
        O(n) to process
        O(n) for result
        create res
        point to left and right
        compare the elements, move the pointers accordingly
        """
        res = [None] * len(nums)
        l, r = 0, len(nums) - 1
        for smaller, greater in zip(range(len(nums)), range(len(nums) -1, -1, -1)):
            if nums[smaller] < pivot:
                res[l] = nums[smaller]
                l += 1
            if nums[greater] > pivot:
                res[r] = nums[greater]
                r -= 1
        while l <= r:
            res[l] = pivot
            l += 1
        return res 
