# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        O(n) to traverse
        O(n) for the stack
        Each node’s value is preceded by a certain number of - characters, which indicates the depth of that node in the tree
        After counting the dashes, we read the next sequence of digits (possibly including a sign if negative values)
        to get the node’s integer value.
        Keep a stack where each element is a node that represents a path down the tree.
        The top of the stack is the most recent (deepest) node
        parse a new node with depth curr_depth:
        Pop from the stack until the stack’s size is exactly curr_depth
        the top of the stack (if it exists) is the new node’s parent.
        Attach the new node as the left child if none exists, otherwise attach it as the right child
        Push the new node onto the stack.
        """
        st, ix, n = [], 0, len(traversal)
        while ix < n:
            curr_depth = 0
            while ix < n and traversal[ix] == '-':
                curr_depth += 1
                ix += 1
            num_starts_ix = ix
            while ix < n and traversal[ix].isdigit():
                ix += 1
            node_val = int(traversal[num_starts_ix:ix])
            node = TreeNode(node_val)

            while len(st) > curr_depth:
                st.pop()
            if st:
                parent = st[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node 
            st.append(node)
        return st[0] if st else None
            