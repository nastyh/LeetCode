# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        m_ix = len(nums) // 2
        t = TreeNode(nums[m_ix])
        t.left = sortedArrayToBST(nums[:m_ix])
        t.right = sortedArrayToBST(nums[m_ix+1:])
        return t
