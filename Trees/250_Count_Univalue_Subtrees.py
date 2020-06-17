def countUnivalSubtrees(self, root):
	 # check if current subtree is uni-value subtree
    def isUni(root,val):
        if not root: return True
        if root.val != val: return False
        if isUni(root.left,val) and isUni(root.right,val):
            return True
        return False
	# recursively check all the nodes
    def dfs(root):
        if not root: return 0
        res = 0
        val1 = dfs(root.left)
        if isUni(root,root.val):   # if current node is uni-value subtree, add 1 to the return value
            res = 1
        val2 = dfs(root.right)
        return val1+val2+res
    
    res = dfs(root)
    return res