# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def constructMaximumBinaryTree(nums):
        def _helper(nums):
            m_ix = nums.index(max(nums))
            res = TreeNode(nums[m_ix])
            if len(nums[:m_ix]) > 0:
                res.left = _helper(nums[:m_ix])
            if len(nums[m_ix + 1:]) > 0:
                res.right = _helper(nums[m_ix + 1:])
            return res

        return _helper(nums)

    # Alternative: actual value instead of the index

    def constructMaximumBinaryTree_alt(nums):
        def _helper(nums):
            m = max(nums)
            res = TreeNode(m)
            if len(nums[:nums.index(m)]) > 0:
                res.left = _helper(nums[:nums.index(m)])
            if len(nums[nums.index[m] + 1:]) > 0:
                res.right = _helper(nums[nums.index[m] + 1:])
            return res

        return _helper(nums)

