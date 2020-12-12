class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def boundary_clockwise(self, root):
        leaves  = []
        left_side = []
        right_side = []
        def _leaves(root):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            _leaves(root.left)
            _leaves(root.right)
        
        def _right_side(root):
            if not root: return
            if root.right:
                right_side.append(root.right.val)
                _right_side(root.right)
            elif root.left:
                right_side.append(root.left.val)
                _right_side(root.left)

        def _left_side(root):
            if not root: return
            if root.left:
                left_side.append(root.val)
                _left_side(root.left)
            elif root.right:
                left_side.append(root.val)
                _left_side(root.left)
        
        _leaves(root)
        _right_side(root)
        _left_side(root)
        return [root.val] + right_side + leaves[::-1][1:] + left_side[1:][::-1]
    

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
    print(l.boundary_clockwise(l))
    print(m.boundary_clockwise(m))
