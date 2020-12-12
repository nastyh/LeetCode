from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def boundaryOfBinaryTree_alt(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        left_boundary = [root.val]
        leaves = []
        right_boundary = []
        if root.left:
            n = root.left
            while n.left or n.right:
                left_boundary.append(n.val)
                if n.left:
                    n = n.left
                else:
                    n = n.right
        if root.right:
            n = root.right
            while n.right or n.left:
                right_boundary.append(n.val)
                if n.right:
                    n = n.right
                else:
                    n = n.left
        def _leaves(root):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            _leaves(root.left)
            _leaves(root.right)
        _leaves(root)
        return left_boundary + leaves + right_boundary[::-1]  


    def boundaryOfBinaryTree(self, root):  # had to write a weird return statement to make it work
        if not root: return []
        left_res = []
        right_res = []
        leaves_res = []
        def _left_helper(node):  # helper to get the left boundary (without the leaves)
            nonlocal left_res
            if node:
                if node.left:
                    left_res.append(node.val)
                    _left_helper(node.left)
                elif node.right:
                    left_res.append(node.val)
                    _left_helper(node.right)
        def _right_helper(node):  # helper to get the right boundary (without the leaves)
            nonlocal right_res
            if node:
                if node.right:
                    right_res.append(node.val)
                    _right_helper(node.right)
                elif node.left:
                    right_res.append(node.val)
                    _right_helper(node.left)
        def _leaves_helper(node):  # just the leaves 
            nonlocal leaves_res
            if node:
                if not node.left and not node.right:
                    leaves_res.append(node.val)
                if node.left:
                    _leaves_helper(node.left)
                if node.right:
                    _leaves_helper(node.right)
        
        if root.left: _left_helper(root)  # without if statements, won't work for some edge cases
        if root.left or root.right: _leaves_helper(root)
        if root.right: _right_helper(root)
        # right_res should be reversed and the first element (head) should be excluded in order to avoid doublecounting 
        return [root.val] + left_res + leaves_res + right_res[1:][::-1] if not root.left else left_res + leaves_res + right_res[1:][::-1]


if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.left = TreeNode(4)
    l.left.right = TreeNode(5)
    l.left.right.left = TreeNode(7)
    l.left.right.right = TreeNode(8)
    l.right.left = TreeNode(6)
    l.right.left.left = TreeNode(9)
    l.right.left.right = TreeNode(10)
    m = TreeNode(1)
    m.right = TreeNode(2)
    m.right.left = TreeNode(3)
    m.right.right = TreeNode(4)

    print(l.boundaryOfBinaryTree_alt(l))
    print(m.boundaryOfBinaryTree_alt(m))
    print(l.boundaryOfBinaryTree(l))
    print(m.boundaryOfBinaryTree(m))
