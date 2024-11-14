class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        O(n) both 
        """
        d_unique = {} # index of each unique element
        num_unique = {} # num of occurances of each unique el (since we're seeing it first)
        res = [0] * len(nums)
        for ix, num in enumerate(nums):
            if num not in d_unique:
                d_unique[num] = ix 
                num_unique[num] = 1
            else:
                d_unique[num] = d_unique[num] + ix
                num_unique[num] = num_unique[num] + 1
        for i in range(len(nums)): #  for each element, calculate the sum of absolute diffs
            res[i] = d_unique[nums[i]] - num_unique[nums[i]]*i     
            d_unique[nums[i]] = d_unique[nums[i]] - 2*i
            num_unique[nums[i]]=num_unique[nums[i]] - 2
        return res
