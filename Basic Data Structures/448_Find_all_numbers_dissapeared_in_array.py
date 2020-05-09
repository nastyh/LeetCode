class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # first solution
        # s = set(nums)
        # return [i for i in range(1,len(nums)+1) if i not in s]

        # second solution

        d = dict(zip(range(1, len(nums)+1),[0]*len(nums)))
        for num in nums:
            if num in d:
                d[num] +=1
        return [k for (k,v) in d.items() if v==0]
