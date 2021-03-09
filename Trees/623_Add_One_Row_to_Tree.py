from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def addOneRow_dfs(self, root, v, d):  # O(n) both
        def dfs(node, v, d, height, direction):
            if not node:
                if height == d:
                    return TreeNode(v)
                else:
                    return None
            if height == d:
                temp = TreeNode(v)
                if direction == 0:
                    temp.left = node
                elif direction == 1:
                    temp.right = node
                return temp
            node.left = dfs(node.left, v, d, height + 1, 0)
            node.right = dfs(node.right, v, d, height + 1, 1)
            return node
        return dfs(root, v, d, 1, 0)
        
    
    def addOneRow_dfs_short(self, root, v, d):
        if d == 1:
            return TreeNode(v, root if left else None, root if not left else None)
        elif root:
            root.left = addOneRow(root.left, v, d - 1, True)
            root.right = addOneRow(root.right, v, d - 1, False)
        return root

    
    def addOneRow_BFS(self, root, v, d):  # O(n) and O(x) where x is the max number of nodes in a level 
        # case when the level is 1
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        dq = deque()
        dq.append(root)
        level = 1
        while level != d - 1:
            for _ in range(len(dq)):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            level += 1
        for _ in range(len(dq)):
            curr = dq.popleft()
            left = curr.left
            right = curr.right
            new1 = TreeNode(v)
            new2 = TreeNode(v)
            curr.left = new1
            new1.left = left
            curr.right = new2
            new2.right = right
        return root
