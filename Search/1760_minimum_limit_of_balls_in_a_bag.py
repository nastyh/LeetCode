class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        O(long(max(nums)) * n), n = len(nums)
        O(1)
        given a max_balls_in_bag, how to distribute the balls so no bag
        contains no more than max_balls_in_bag and it's done in maxOperations?
        A valid distribution is possible if and only if the total number of operations across all bags is less than or equal to maxOperations
        sum(operations_i) <= maxOperations

        binary search on the possible penalty values from 1 to max(nums)
        can_penalize --> whether it's possible to achieve a given penalty value 
        within the given number of operations 
        For each bag:
        1. calc how many splits are required to ensure no bag exceeds the given penalty
        2. formula for splits: (balls-1) // penalty 

        sum the splits across all the bags
        check if the total splits are <= maxOperations
        """
        nums.sort()
        def _helper(penalty):
            ops = 0
            for num in nums:
                if num > penalty:
                    ops += (num - 1) // penalty
            return ops <= maxOperations
        l, r = 1, max(nums)
        while l < r:
            m = l + (r - l) // 2
            if _helper(m):
                r = m # trying a smaller penalty
            else:
                l = m + 1 # trying a larger penalty 
        return l 
        
