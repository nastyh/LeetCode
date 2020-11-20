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

def countUnivalSubtrees_alt(self, root):
    # at any point if you know two things:
    # 1) count of univalue subtrees from its left descendants and if its a univalue subtree
    # 2) count of univalue subtrees from its right descendants and if its a univalue subtree
    # Then you can easily calculate outcome of the current level
    
    # count to return will atleast be sum of 1) and 2) 
    
    # Only two possible scenarios for the current level:
    # 1) Add +1 to count and return True if both left/(and)right subtrees are univalue and value of left,right and current level is the same i.e. it is a univalue subtreee
    # 2) keep count same and return False if the current level is not a univalue subtree 
    
    # just handle some corner cases and we are done
    
        def count_subtree(root):
            """
            return: count, boolean indicating if its a univalue subtree
            """
            if not root:
                return 0, False
            
            if not root.left and not root.right:
                return 1, True
            
            left_count, left_is_univalue = count_subtree(root.left)
            
            right_count, right_is_univalue = count_subtree(root.right)
            
            
            if root.left and root.right: 
                if left_is_univalue and right_is_univalue:
                    if root.left.val == root.right.val == root.val:
                        return left_count + right_count + 1, True
            elif root.left and left_is_univalue:
                if root.left.val == root.val:
                    return left_count + right_count + 1, True
            elif root.right and right_is_univalue:
                if root.right.val == root.val:
                    return left_count + right_count +1 , True

            return left_count + right_count, False
    count, is_uni = count_subtree(root)
    return count