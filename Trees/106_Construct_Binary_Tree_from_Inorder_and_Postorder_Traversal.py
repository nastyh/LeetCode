# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def buildTree(self, inorder, postorder):  # O(n) both 
        if inorder:
            root_val = postorder[-1]
            root = TreeNode(root_val)
        else:
            return None

        ix_of_root_in_inorder = inorder.index(root_val)
        root.left = buildTree(inorder[:ix_of_root_in_inorder], postorder[:ix_of_root_in_inorder])
        root.right = buildTree(inorder[ix_of_root_in_inorder+1:], postorder[ix_of_root_in_inorder:-1])
        return root

    
    def buildTree_stack(self, inorder, postorder):  # using stack. Works faster 
        if not postorder:
            return None
        postIter = reversed(postorder)
        root = TreeNode(next(postIter))
        parentStack = [root]
        
        i = len(inorder) - 1
        for val in postIter:
            node = TreeNode(val)
            if inorder[i] == parentStack[-1].val:
                i -= 1
                parent = parentStack.pop()
                
                while parentStack and inorder[i] == parentStack[-1].val:
                    parent = parentStack.pop()
                    i -= 1
                
                parent.left = node
                parentStack.append(node)
                
            else:    
                parentStack[-1].right = node
                parentStack.append(node)

        return root   