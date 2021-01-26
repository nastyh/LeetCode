class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def pathSum(self, root):
        def _helper(root, curr_sum):
            if not root:
                return 0
            if root and (not root.left and not root.right):
                curr_sum += root.val
                return curr_sum
            return _helper(root.left, curr_sum) 

        return _helper(root, 0)
    
    def sumOfAllLeaves(self, root): # just returns a number
        res = 0
        if not root:
            return res
        if root:
            res += root.val
        return res + self.sumOfAllLeaves(root.left) + self.sumOfAllLeaves(root.right)]

    
    def binaryTreePaths(self, root):  # DFS. O(n) and O(n). Space to be exact is O(n*h^2), where h is the diameter, b/c of the overhead to build "->" lines
        """
        Just DFS using the helper function. 
        Terminating condition first.
        If no, add a current value to the path and append it at the end once you hit a leaf node. 
        """
        def _allPaths(root, path):
            # res = []
            if root and not root.left and not root.right:
                self.res.append(path)        
            if root.left:    
                _allPaths(root.left, path + '->' + str(root.left.val))
            if root.right:
                _allPaths(root.right, path + '->' + str(root.right.val))   
        self.res = []
        if not root:
            return res
        _allPaths(root, str(root.val))
        return self.res


    def binaryTreePaths_stack(self, root):  # O(n) and O(n)
        if not root:
            return []
        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        return paths

    def binaryTreePaths_alt(self, root):
        """
        More straigthforward:
        create a list of lists with values
        Then turn it into a list with strings as the question asks 
        """
        if not root: return None
        if root and not root.left and not root.right: return [str(root.val)]
        values = []
        def _helper(node, lists):
            if not node: return
            if node and not node.left and not node.right:
                lists.append(node.val)
                values.append(lists)
            if node.left: _helper(node.left, lists + [node.val])
            if node.right: _helper(node.right, lists +  [node.val])
        _helper(root, [])
        res = []
        for el in values:
            ans = ''
            for num in el:
                ans += str(num)
                ans += '->'
            res.append(ans[:-2])
        return res
      

if __name__ == '__main__': 
      
    # binary tree formation  
    l = TreeNode(1)  
    l.left = TreeNode(2)  
    l.right = TreeNode(3)  
    # l.left.left = TreeNode(1)  
    l.left.right = TreeNode(5)  
    # l.right.left = TreeNode(11)  
    # l.right.right = TreeNode(13)
    # print(l.binaryTreePaths(l))  
    print(l.binaryTreePaths_alt(l))  
