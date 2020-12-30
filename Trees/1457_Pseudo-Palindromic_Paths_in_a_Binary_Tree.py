from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def pseudoPalindromicPaths (self, root):  #O(n) and O(h) where h is the height?
        """
        _helper function creates a list with path values.
        Once a list is created _checker checks if there are 0 or 1 elements that occur the odd number of times.
        If it's a case, then it's a palindrome (2, 2, 1) or (6, 6, 7, 7) and increment res 
        """
        if not root: return 0
        if root and not root.left and not root.right: return 1
        res = 0
        def _checker(nums):
            odds = 0
            d = Counter(nums)
            for v in d.values():
                if v % 2 == 1:
                    odds += 1
                if odds > 1:
                    return False
            return True
        def _helper(node, curr_path):
            nonlocal res
            if not node: return
            if node and not node.left and not node.right:
                if _checker(curr_path):
                    res += 1
            if node.left:
                _helper(node.left, curr_path + [node.left.val])
            if node.right:
                _helper(node.right, curr_path + [node.right.val])
        _helper(root, [root.val])
        return res

    
    def pseudoPalindromicPaths_recursive_XOR(self, root):
        """
        The idea is to keep the frequency of digit 1 in the first bit, 2 in the second bit,
        etc: path ^= (1 << node.val).
        """
        def preorder(node, path):
            nonlocal count
            if node:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:                    
                    preorder(node.left, path)
                    preorder(node.right, path) 
        
        count = 0
        preorder(root, 0)
        return count

    
    def pseudoPalindromicPaths_iter_XOR(self, root):
        count = 0
        stack = [(root, 0)]
        while stack:
            node, path = stack.pop()
            if node is not None:
                # compute occurences of each digit 
                # in the corresponding register
                path = path ^ (1 << node.val)
                # if it's a leaf, check if the path is pseudo-palindromic
                if node.left is None and node.right is None:
                    # check if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.right, path))
                    stack.append((node.left, path))
        
        return count


if __name__ == '__main__':
    l = TreeNode(2)
    l.left = TreeNode(3)
    l.left.left = TreeNode(3)
    l.left.right = TreeNode(1)
    l.right = TreeNode(1)
    l.right.right = TreeNode(1)
    print(l.pseudoPalindromicPaths(l))
    m = TreeNode(2)
    m.left = TreeNode(1)
    m.left.left = TreeNode(1)
    m.left.right = TreeNode(3)
    m.left.right.right = TreeNode(1)
    m.right = TreeNode(1)
    print(m.pseudoPalindromicPaths(m))