"""
Given a list with values. Check if the sequence of values is present in the tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def find_path(self, root, sequence):
        def _helper(root, sequence):
            if not root: return False
            if root and not root.left and not root.right and len(sequence) == 1 and root.val == sequence[0]:
                return True
            if root.val != sequence[0]:
                return False
            return _helper(root.left, sequence[1:]) or _helper(root.right, sequence[1:])
        return _helper(root, sequence)


if __name__ == '__main__':
  l = TreeNode(1)
  l.left = TreeNode(0)
  l.right = TreeNode(1)
  l.left.left = TreeNode(1)
  l.right.left = TreeNode(6)
  l.right.right = TreeNode(5)

  print(l.find_path(l, [1, 0, 7]))
  print(l.find_path(l, [1, 1, 6]))
  print(l.find_path(l, [1, 1, 5]))