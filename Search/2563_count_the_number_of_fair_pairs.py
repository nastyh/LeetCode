class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        O(nlogn) and O(1)
        """
        l, r, res = 0, len(nums) - 1, 0
        l1, r1 = 0, len(nums) - 1
        res_lower, res_upper = 0, 0
        nums.sort()
        while l < r:
            """
            calculate how many pairs give the sum < lower
            calculate how many pairs give the sum <= upper 
            Second minus first is the answer: within the desired range
            """
            if nums[l] + nums[r] < lower:
                res_lower += (r - l)
                l += 1
            else:
                r -= 1
        while l1 < r1:
            if nums[l1] + nums[r1] <= upper:
                res_upper += (r1 - l1)
                l1 += 1
            else:
                r1 -= 1
        return res_upper - res_lower

    def countFairPairs_cleaner(self, nums: List[int], lower: int, upper: int) -> int:
        """
        O(nlogn) and O(1)
        """
        nums.sort()
        def _helper(nums, k):
            """
            just move the logic to the helper function 
            """
            i, j, res = 0, len(nums) - 1, 0
            while i < j:
                if nums[i] + nums[j] <= k:
                    res += j - i 
                    i += 1
                else:
                    j -= 1
            return res
        lower_res = _helper(nums, lower - 1) # since we need to the left of lower only, b/c ==lower is a good answer
        upper_res = _helper(nums, upper)
        return upper_res - lower_res

    def countFairPairs_with_mid(self, nums: List[int], lower: int, upper: int) -> int:
        """
        all the same but the helper function 
        uses the mid element in calculations 
        """
        nums.sort()
        res = 0
        def _lower_helper(nums, k, start):
            l, r = start, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < k:
                    l = m + 1
                else: 
                    r = m
            return l
        
        def _upper_helper(nums, k, start):
            l, r = start, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] <= k:
                    l = m + 1
                else:
                    r = m 
            return l 
        
        for i in range(len(nums)):
            l = _lower_helper(nums, lower - nums[i], i + 1)
            r = _upper_helper(nums, upper - nums[i], i + 1)
            res += r - l
        return res