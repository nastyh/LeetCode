from collections import deque 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def hasPathSum(self, root, s):
        if not root:
            return False
        if root and (not root.left and not root.right):
            return root.val == s
        else:
            return self.hasPathSum(root.left, s - root.val) or self.hasPathSum(root.right, s - root.val)

    
    def hasPathSum_another(self, root, s):
        """
        key here is to write return l or r. Because otherwise, if the very left subtree isn't True,
        it will immediately return False to everything
        """
        def _helper(node, num):
            if not node: return 
            if  node.val == num and not node.left and not node.right:
                return True
            l, r = False, False
            if node.left: 
                l = _helper(node.left, num - node.val)
            if node.right:
                r = _helper(node.right, num - node.val)
            return l or r
        return _helper(root, s)

    
    def hasPathSum_DFS(self, root, s):
        if not root: return False
        if root and not root.left and not root.right:
            if root.val == s:
                return True
            else:
                return False
        def _helper(node, s):
            if not node: return False 
            if node and not node.left and not node.right:
                return s == node.val
            return _helper(node.left, s - node.val) or _helper(node.right, s - node.val)
            return False
        return _helper(root, s)


    def hasPathSum_iter(self, root, s):
        if not root: return False
        stack = [(root, s)]
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right and node.val == s:
                return True
            if node.left:
                stack.append((node.left, s - node.val))
            if node.right:
                stack.append((node.right, s - node.val))
        return False

    
    def hasPathSum_BFS(self, root, s):  # doesn't work
        if not root:
            return False
        q = deque()
        q.append([root, 0])       
        while q:
            t = q.popleft()
            t[1] =+ t[0].val
            if (not t[0].left and not t[0].right):
                return t[1] == s
            else:
                if t[0].left:
                    q.append([t[0].left, t[1]])
                if t[0].right:
                    q.append([t[0].right, t[1]])
        return False


if __name__ == '__main__':
    l = TreeNode(5)
    l.left = TreeNode(4)
    l.right = TreeNode(8)
    l.left.left = TreeNode(11)
    l.right.left = TreeNode(13)
    l.right.right = TreeNode(4)
    l.left.left.left = TreeNode(7)
    l.left.left.right = TreeNode(2)
    l.right.right.right = TreeNode(1)
    print(l.hasPathSum(l, 22))
    print(l.hasPathSum_iter(l, 22))
    print(l.hasPathSum_DFS(l, 22))
    # print(l.hasPathSum_BFS(l, 22))
            
            
        