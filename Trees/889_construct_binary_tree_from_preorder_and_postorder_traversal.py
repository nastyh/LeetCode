# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost_optimal(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        O(n) for n lookups in the dict
        O(n) due to the dict and the recursion stack 
        Preorder: root, left, right
        Postorder: left, right, root
        The dictionary post_idx maps each value in the postorder array to its corresponding index.
        This allows for O(1) lookup when determining the size of the left subtree.
        The value preorder[pre_start + 1] is the root of the left subtree.
        Its index in the postorder array is fetched using the precomputed dictionary, and the size of the left subtree is calculated accordingly.
        The left and right subtrees are constructed recursively by adjusting the index ranges.

        _helper uses indices to avoid slicing the lists
        pre_start and pre_end denote the current range in the preorder list.
        post_start and post_end denote the current range in the postorder list.
        """
        post_idx = {val: i for i, val in enumerate(postorder)}
        def _helper(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            # The first element in preorder is the root.
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            # The second element in preorder is the root of the left subtree.
            left_root_val = preorder[pre_start + 1]
            # Determine the size of the left subtree using the precomputed index.
            left_subtree_size = post_idx[left_root_val] - post_start + 1
            
            # Recursively construct the left subtree.
            root.left = _helper(pre_start + 1, pre_start + left_subtree_size,
                            post_start, post_idx[left_root_val])
            # Recursively construct the right subtree.
            root.right = _helper(pre_start + left_subtree_size + 1, pre_end,
                                post_idx[left_root_val] + 1, post_end - 1)
            return root

        return _helper(0, len(preorder) - 1, 0, len(postorder) - 1)
    
    def constructFromPrePost_recursion(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        O(n^2) in case of the skewed tree due to recursive calls and slicing
        O(n) due to the recursion stack
        Recursive approach
        The first element of preorder is taken as the root of the tree.
        Find this element in the postorder list.
        Its index (plus one) gives the number of nodes in the left subtree.
        Slice the preorder and postorder arrays accordingly and recursively construct the left and right subtrees.
        """
        if not preorder: # edge case
            return None
        # The first element in preorder is the root.
        root = TreeNode(preorder[0])
        # If there's only one element, it's a leaf node.
        if len(preorder) == 1:
            return root

        # The second element in preorder is the root of the left subtree.
        left_root_val = preorder[1]
        # Find the index of this value in postorder to determine the left subtree's size.
        left_subtree_size = postorder.index(left_root_val) + 1

        # Recursively construct the left and right subtrees.
        root.left = self.constructFromPrePost(preorder[1:left_subtree_size+1], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size+1:], postorder[left_subtree_size:-1])
        
        return root