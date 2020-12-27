def longestConsecutive(self, root):
    longest = 0
    def dfs(self, node):
        if node is None: 
            return (0, 0)
        left, right = node.left, node.right
        l_inc, l_dec = self.dfs(left)
        r_inc, r_dec = self.dfs(right)
        n_inc = n_dec = 1
        if left and left.val + 1 == node.val:
            n_inc = l_inc + 1
        if right and right.val + 1 == node.val:
            n_inc = max(n_inc, r_inc + 1)
        if left and left.val - 1 == node.val:
            n_dec = l_dec + 1
        if right and right.val - 1 == node.val:
            n_dec = max(n_dec, r_dec + 1)        
        self.longest = max(self.longest, n_inc + n_dec - 1)
        return(n_inc, n_dec)
        
        self.dfs(root)
        return self.longest 
        
    