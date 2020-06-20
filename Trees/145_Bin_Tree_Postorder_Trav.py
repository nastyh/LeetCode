# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def postorderTraversal(self, root):
        if not root:
            return []

        stack ,out= [], []
        node, prev = root, None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            # add check to see if right leaf was the last seen
            if not node.right or node.right == prev:
                prev = stack.pop()
                out.append(node.val)
                node = None
            # iterate to right subtree
            else:
                node = node.right
        return out

    def postorderTraversal_alt(self, root):
        stack, result = [], []
        while stack or root:
            while root:
                if root.right: stack.append(root.right)
                stack.append(root)
                root = root.left
            node = stack.pop()
            if stack and stack[-1] is node.right:
                root = stack.pop()
                stack.append(node)
            else:
                result.append(node.val)
        return result

    def postorderTraversal_2_stacks(self, root):
        stack = [root] if root else None
        res = []
        
        while stack:
            # pop top of first stack and push it to the second
            curr = stack.pop()
            res.append(curr.val)
            
            # traverse
            if curr.left:
                stack.append(curr.left)
                
            if curr.right:
                stack.append(curr.right)
                
        # reversed second stack gives us our answer        
        return res[::-1]

    def postorderTraversal_flags(self, root):
        stack=[(False,root)]
        res=[]
        while stack:
            flag,val=stack.pop()
            if val:
                if not flag:
                    stack.append((True,val))
                    stack.append((False,val.right))
                    stack.append((False,val.left))
                else:
                    res.append(val.val)
        return res


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(2)
    l.right = TreeNode(6)
    l.left.left = TreeNode(1)
    # l.right.left = TreeNode(2)
    l.left.right = TreeNode(3)

print(l.postorderTraversal(l))
print(l.postorderTraversal_alt(l))
print(l.postorderTraversal_2_stacks(l))
print(l.postorderTraversal_flags(l))
