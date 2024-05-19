class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #start by having a list of size k
        # its left side is index 0, the right side is index k - 1
        # we will move to the right by 
        # subtracting the element at index l_ix and adding the element at r_ix
        # so it's easier to compute the running array 
    if len(nums) == k:
        return sum(nums) / k 
    r_ix = k
    l_ix = 0
    glob_sum, curr_sum = sum(nums[:r_ix]), sum(nums[:r_ix]) # should be initialized as such
    while r_ix < len(nums):
        curr_sum = curr_sum - nums[l_ix] + nums[r_ix]
        glob_sum = max(glob_sum, curr_sum)
        l_ix += 1
        r_ix += 1
    return glob_sum / k