# cousing are nodes that have the same depth but different parents
from collections import deque
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isCousins_BFS(self, root, x, y): # bfs

        q = deque([(root, 0, None)])
        x_info = y_info = None  # Will store (level, parent) for x and y
        
        while q:
            node, level, parent = q.popleft()
            if node.val == x:
                x_info = (level, parent)
            if node.val == y:
                y_info = (level, parent)
            # If we've found both, we can break early
            if x_info and y_info:
                break
            if node.left:
                q.append((node.left, level + 1, node))
            if node.right:
                q.append((node.right, level + 1, node))
                
        # Two nodes are cousins if they are on the same level but have different parents.
        return x_info is not None and y_info is not None and (x_info[0] == y_info[0]) and (x_info[1] != y_info[1])

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
