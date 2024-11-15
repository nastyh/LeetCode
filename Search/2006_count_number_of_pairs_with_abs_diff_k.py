class Solution:
    def countKDifference_dict(self, nums: List[int], k: int) -> int:
        """
        O(n) both
        dict as element: number of times we see it
        """
        d = Counter(nums)
        res = 0
        for num in nums:
            if num + k in d: # if there is a complement to num
                res += d[num+k] # add how many times this complement exists to res 
        return res
    
    def countKDifference_brute_force(self, nums: List[int], k: int) -> int:
        """
        O(n^2) and O(1)
        Just two loops to check each possible pair 
        """
        res = 0
        for l in range(len(nums)-1):
            for r in range(l + 1, len(nums)):
                if abs(nums[l] - nums[r]) == k:
                    res += 1
        return res