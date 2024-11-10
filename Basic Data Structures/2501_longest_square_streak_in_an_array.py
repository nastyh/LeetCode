class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        O(n) both 
        create a with the numbers
        when we find a square, increment this element 
        """
        d = {num:1 for num in nums}
        res = 0
        for num in nums:
            curr = 1
            if math.sqrt(num) not in d:
                j = num*num
                while j in d:
                    curr += 1
                    j = j*j
            res = max(res, curr)
        return res if res > 1 else -1

    def longestSquareStreak_set(self, nums: List[int]) -> int:
        """
        O(nlogn) and O(n)
        set since the same numbers can be squares
        go through, till we can find the squared numbers, add to l
        take the largest 
        """
        s = set(nums)
        res = 1
        for num in s:
            squared = num**2
            l = 1
            while squared in s:
                squared = squared**2
                l += 1
            res = max(res, l)
        return res if res > 1 else -1
            