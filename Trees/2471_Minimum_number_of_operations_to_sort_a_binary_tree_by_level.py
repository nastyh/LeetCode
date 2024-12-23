# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """
        O(nlogn) for all the sorting
        O(n) for building a list of lists and the dictionaries 
        the core question here is in _helper()
        It takes a list and counts the number of swaps needed to be completed 
        to make this list sorted 
        We sort it, save in correct_nums, build a dictionary value: index based off of correct_nums
        then go over nums and compare.
        Also need to make the swaps if the order is off so we can continue moving

        The other part does a usual BFS thing: create a list of lists w/ values by level
        Then use _helper on each list and return the result
        """
        def _helper(nums):
            res, correct_nums = 0, sorted(nums)
            d = {val: ix for ix, val in enumerate(nums)}
            for i in range(len(nums)):
                if nums[i] != correct_nums[i]:
                    res += 1
                    curr_pos = d[correct_nums[i]]
                    d[nums[i]] = curr_pos
                    nums[curr_pos] = nums[i]
            return res
        
        if not root: return  
        all_levels, d = [], deque()
        d.append(root)
        while d:
            curr_level = []
            len_d = len(d)
            for _ in range(len_d):
                t = d.popleft()
                curr_level.append(t.val)
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            all_levels.append(curr_level)

        return sum([_helper(l) for l in all_levels])