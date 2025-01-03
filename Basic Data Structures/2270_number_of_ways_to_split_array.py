class Solution:
    def waysToSplitArray_just_sum_variables(self, nums: List[int]) -> int:
        """
        O(n) and O(1)
        just go over the list and increment the left sum and decrement the right sum
        compare and build res
        """
        l_sum, r_sum = 0, sum(nums)
        res = 0
        for candidate in nums[:-1]:
            l_sum += candidate
            r_sum -= candidate
            if l_sum >= r_sum:
                res += 1
        return res
        
    def waysToSplitArray_running_sums(self, nums: List[int]) -> int:
        """
        O(N) both
        to calculate and store the running sums
        two lists: first in left is nums[0], others are being added up
        right: last one is nums[-1], others are added up
        Noticed on paper that left[0] >= right[1] is the key
        so iterate over both and if you see it, increment res 
        """
        res = 0
        left_running_sum, right_running_sum = [0] * len(nums), [0] * len(nums)
        left_running_sum[0], right_running_sum[-1] = nums[0], nums[-1] # first and last elements in the running lists
        for i in range(1, len(nums)): #populate left
            left_running_sum[i] = left_running_sum[i-1] + nums[i]
        for i in range(len(nums) -2, -1, -1): # populate right
            right_running_sum[i] = right_running_sum[i+1] + nums[i]
        for i in range(1, len(nums)): # compare 
            if left_running_sum[i-1] >= right_running_sum[i]:
                res += 1
        return res
    def waysToSplitArray_brute_force(self, nums: List[int]) -> int:
        """
        O(n^2) and O(1)
        easy to understand:
        have a pointer going to the second to last element
        recalculate the left sum 
        right sum is slighly optimized by doing sum_of_nums minus left_part
        Works but times out 
        """
        res = 0
        sum_of_nums = sum(nums)
        for i in range(len(nums)-1):
            left_part = sum(nums[:i +1])
            right_part = sum_of_nums - left_part
            if left_part >= right_part:
                res += 1
        return res