# cousing are nodes that have the same depth but different parents
from collections import deque
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isCousins_BFS(self, root, x, y): # bfs

        def _parent(root, value_to_find, parent, level): # returns [level, parent as integer]
            if not root:
                return None, parent_val
            res = []

            q = deque()
            q.append([root, value_to_find, None, 0]) # order is root, value_to_find, parent, level
            while q:
                t, curr_val, curr_parent, curr_level = q.popleft()
                if t.val == curr_val:
                    res.append(curr_level)
                    res.append(curr_parent.val)
                if t.left:
                    q.append([t.left, value_to_find, t, curr_level + 1])
                if t.right:
                    q.append([t.right, value_to_find, t, curr_level + 1])

            return res

        x_info = _parent(root, x, None, 0)
        y_info = _parent(root, y, None, 0)

        if x_info[1] != y_info[1] and x_info[1] != y_info[1]:
            return True
        else:
            return False

    def isCousins_DFS_alt(self, root, x, y):
        if not root: return

        def _helper(root, value_to_find, parent, level):
            if not root: return

            if root.val == value_to_find:
                return [parent.val, level]
            else:
                l =_helper(root.left, value_to_find, root, level + 1)
                r = _helper(root.right, value_to_find, root, level + 1)
                if l: return l
                if r: return r


        x_res = _helper(root, x, None, 0)
        y_res = _helper(root, y, None, 0)

        if x_res[0] != y_res[0] and x_res[1] == y_res[1]:
            return True
        else:
            return False

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.right = TreeNode(5)
    print(l.isCousins_BFS(l, 4, 5))
    print(l.isCousins_DFS_alt(l, 4, 5))
