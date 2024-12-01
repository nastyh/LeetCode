class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        """
        O(n) both
        set for quick checks 
        we will do at most len(nums) runs overall 
        if curr number (kept in curr) is originally in nums,
        update curr to 2*curr and keep working 
        Else, return curr w/o updating it 
        """
        curr = original
        s = set()
        for n in nums:
            s.add(n)
        for _ in range(len(nums)):
            if curr in s:
                curr *= 2 
            else:
                return curr
        return curr 