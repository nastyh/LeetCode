from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

    def findNearestRightNode_optimized(self, root, u):  # O(n) and O(1)
        if not root: return Null
        if root and not root.left and not root.right:
            if root.val == u.val:
                return None
        d = deque()
        d.append(root)
        while d:
            size = len(d)  # that is important, otherwise will be an error if u == most right element
            for ix in range(size):
                t = d.popleft()
                if t.val == u.val:
                    if ix != size - 1:
                        return d.popleft()
                    else:
                        return None
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)


    def findNearestRightNode(self, root, u):  #  O(n) and O(n)
        """
        brute force: collect everything and check
        """
        if not root: return None
        if root and not root.left and not root.right:
            if root.val == u.val:
                return None
        d = deque()
        d.append(root)
        res = []
        while d:
            curr_level = []
            for ix in range(len(d)):
                t = d.popleft()
                curr_level.append(t.val)
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            res.append(curr_level)
        for level in res:
            for ix in range(len(level)):
                if level[ix] == u.val:
                    if ix == len(level) - 1:
                        return Null
                    else:
                        return level[ix + 1]


    def findNearestRightNode_DFS(self, root, u):  # O(N) and O(H) for the stack
        def preorder(node, depth):
            nonlocal u_depth, next_node
            # the depth to look for next node is identified
            if node == u:
                u_depth = depth
            # we're on the level to look for the next node
            elif depth == u_depth:
                # if this next node is not identified yet
                if next_node is None:
                    next_node = node  
            # continue to traverse the tree
            else:
                for child in [node.left, node.right]:
                    if child:
                        preorder(child, depth + 1)
        u_depth, next_node = -1, None
        preorder(root, 0)
        return next_node


if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.right = TreeNode(4)
    l.right.left = TreeNode(5)
    l.right.right = TreeNode(6)
    # print(l.findNearestRightNode(l, l.left.right))
    print(l.findNearestRightNode_optimized(l, l.left.right))