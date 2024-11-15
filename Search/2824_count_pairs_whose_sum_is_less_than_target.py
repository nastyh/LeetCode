class Solution:
    def countPairs_brute_force(self, nums: List[int], target: int) -> int:
        """
        O(n^2) and O(1)
        basic: calculate each possible pair with a double loop
        if the sum < target, increment res 
        """
        res = 0
        for l in range(0, len(nums) -1):
            for r in range(l+1, len(nums)):
                if nums[l] + nums[r] < target:
                    res += 1
        return res 

    def countPairs_binary(self, nums: List[int], target: int) -> int:
        """
        O(nlogn) for sorting
        O(1)
        """
        l, r, res = 0, len(nums) - 1, 0
        nums.sort()
        while l < r:
            if nums[l] + nums[r] < target:
                """
                it means that if we keep l fixed and move r to the left,
                the sum will become even smaller. So everything with the current l
                is good to go: increment res by the diff of indices
                Move l to the right to make it bigger and reassess the situation
                """
                res = res + (r - l)
                l += 1
            else:
                """
                r is too big. We need to move to the left and hope 
                it will make the sum < target 
                """
                r -=1
        return res

                