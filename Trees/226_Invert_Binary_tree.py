# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #DFS
        # if not root:
        #     return None
        # # if not root.left and not root.right:
        # #     return root
        # # if root.left and not root.right:
        # #     return None
        # # if not root.left and root.right:
        # #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        #BFS
        from collections import deque
        if not root:
            return None
        s = deque()
        s.append(root)
        while s:
            t = s.popleft()
            if t:
                t.left, t.right = t.right, t.left
                s.extend([t.right, t.left])
                # if t.left:
                #     s.append(t.right)
                # if t.right:
                #     s.append(t.left)
        return root
