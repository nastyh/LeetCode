# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def countNodes_bfs(self, root):  # O(n) and O(1)
        if not root: return 0
        if root and not root.left and not root.right: return 1
        d = deque()
        res = 0
        d.append(root)
        res += 1
        while d:
            t = d.popleft()
            if t.left:
                d.append(t.left)
                res += 1
            if t.right:
                d.append(t.right)
                res += 1
        return res

    
    def countNodes_dfs(self, root):  #O(n) and O(d), where d is the depth of the tree, in this case it's logn. So space is O(logn)
        if not root: return 0
        if root and not root.left and not root.right: return 1
        res = 0
        def _helper(node):
            nonlocal res
            if not node: return
            _helper(node.left)
            res += 1
            _helper(node.right)
        _helper(root)
        return res


    def countNodes_log(self, root):  # O(logn) for tree traversal and O(logn) for searching the last row. Overall, O(log^2(n)). Space is O(1)
        """
        The height of the tree is h; therefore, there are 2^h nodes in the last row of the tree.
        start by checking the middle of the last row, which is 2^(h-1). If it was present, then check the middle element of the right side,
        and otherwise check the middle element of the left side, and continue this trend until we reach a position where the difference between
        the position of a present element and a null pointer is just one.
        The mid variable gets a value of 0 to 2^h. The binary representation is checked bit by bit from the most significant digit to the least.
        If it is a one, we go to the right child, and if it is zero, we go to the left child. This way, a single number represents the path we go
        to reach the last row of the tree. For example, for a tree with a depth of 3, there are 8 nodes in the last row. The number 4 for tree traversal is
        100, which means root goes to the right child, then left child, and then again the left child to reach the last row.
        """
        height = 0
        node = root
        while node:
            node = node.left
            height += 1
        lastLevel = int(pow(2, height - 1))
        lastPresent = 0
        lastNotPresent = lastLevel
        while (lastNotPresent - lastPresent > 1):
            mid = (lastNotPresent + lastPresent) // 2
            bit = lastLevel >> 1
            node = root
            while (bit > 0):
                if (mid & bit):
                    node = node.right
                else:
                    node = node.left
                bit >>= 1
            if (node):
                lastPresent = mid
            else:
                lastNotPresent = mid
        return lastLevel + lastPresent


    def countNodes_nlogn(self, root):  # O(nlogn) both
        """
        Number of Nodes = 2 ** (level number) - 1 + final level nodes number
        """
        if not root:
            return 0
        self.last_level_count = 0
        self.level = 0
        # Stop flag to end searching
        self.stop = 0
        def dfs(node, level):
            if self.stop:
                return
            if not node:
                self.level = max(self.level, level)
                # If the reaches the final level, then count 1
                # Note this is actually counting for # of children (None) of final level nodes
                if self.level == level:
                    self.last_level_count += 1
                else:
                    self.stop = 1
                return
            self.dfs(node.left, level + 1)
            self.dfs(node.right, level + 1)
        # Start with -1 since the searching ends on the children of leafs (None)
        # Make -1 offset then self.level can be the real value
        dfs(root, -1)
        return 2 ** self.level - 1 + self.last_level_count // 2
        



if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.left = TreeNode(4)
    l.left.right = TreeNode(5)
    l.right.left = TreeNode(6)
    # l.right.right = TreeNode(14)
    print(l.countNodes_bfs(l))


