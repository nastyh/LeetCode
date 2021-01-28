class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def mergeTrees(self, t1, t2): # recursive approach creating a new tree
         if not t1 and not t2:
             return None
         if t1 and not t2:
             return t1
         if not t1 and t2:
             return t2
         t3 = TreeNode(t1.val + t2.val)
         t3.left = self.mergeTrees(t1.left, t2.left)
         t3.right = self.mergeTrees(t1.right, t2.right)
         return t3
         
    
    def mergeTrees_dfs(self, t1, t2):  # O(n) both. Space on average will be O(logn)
        if not t1 and not t2: return None
        if t1 and not t2: return t1
        if not t1 and t2: return t2
        def _helper(n1, n2):
            if not n1: return n2
            if not n2: return n1
            if n1 and n2:
                n1.val += n2.val
            n1.left = _helper(n1.left, n2.left)
            n1.right = _helper(n1.right, n2.right)
            return n1.val
        return _helper(t1, t2)
        
         
    def mergeTrees(self, t1, t2): # level-order
        if not t1:
            return t2
        if not t2:
            return t1
        # new node val
        def nodeSum(node1, node2):
            if not node1:
                return node2.val
            if not node2:
                return node1.val
            return node1.val + node2.val

        root = TreeNode(t1.val + t2.val)
        queue = [[root, t1, t2]]
        while queue:
            t = queue.pop()
            if t[1] or t[2]:
                # left child
                n1 = t[1].left if t[1] else None
                n2 = t[2].left if t[2] else None
                if n1 or n2:
                    t[0].left = TreeNode(nodeSum(n1, n2))
                    queue.append([t[0].left, n1, n2])
                # right child
                n1 = t[1].right if t[1] else None
                n2 = t[2].right if t[2] else None
                if n1 or n2:
                    t[0].right = TreeNode(nodeSum(n1, n2))
                    queue.append([t[0].right, n1, n2])
        return root


if __name__ == '__main__':   
    l = TreeNode(1)
    l.left = TreeNode(3)
    l.right = TreeNode(2)
    l.left.left = TreeNode(5)
    m = TreeNode(2)
    m.left = TreeNode(1)
    m.right = TreeNode(3)
    m.left.right = TreeNode(4)
    m.right.right = TreeNode(7)
    print(l.mergeTrees_dfs(l, m))
        
         