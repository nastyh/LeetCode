# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):  # O(h) both 
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# iteratively
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Value of p
        p_val = p.val
        # Value of q
        q_val = q.val
        # Start from the root node of the tree
        node = root
        # Traverse the tree
        while node:
            # Value of current node or parent node.
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node
