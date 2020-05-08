class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {} # build a dict w/ frequencies of elements
        for num in nums:
            if num in d:
                d[num] +=1
            else:
                d[num] = 1
        return [k for (k,v) in d.items() if v>len(nums)/2][0] # return the key with the value >len(nums)/2. [0] is needed b/c otherwise it returns a list with one element, and we need to return a number

