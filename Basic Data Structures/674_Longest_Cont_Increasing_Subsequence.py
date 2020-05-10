class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        if len(set(nums)) == 1:
            return 1
        counter, gl_m = 1, 0
        for n_ix in range(len(nums)-1):
            if nums[n_ix] < nums[n_ix + 1]:
                counter +=1
                gl_m = max(gl_m, counter)
            else:
                counter = 1
                gl_m = max(gl_m, counter)
        return gl_m
