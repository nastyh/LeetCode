# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def pathSum(self, root, s):
        if not root: return []
        if root and not root.left and not root.right:
            if root.val == s:
                return [[s]]
            else:
                return []
        res = []
        def _helper(root, s, path):
            if not root: return
            if root and not root.left and not root.right:
                if s == root.val:
                    path.append(root.val)
                    res.append(path)
            if root.left:
                _helper(root.left, s - root.val,  path + [root.val])
            if root.right:
                _helper(root.right, s - root.val, path + [root.val])
        _helper(root, s, [])
        return res

    def pathSum_stupid(self, root, s):
        """
        Create a list of lists with all root-to-leaf paths and return only those that add up to s
        """
        if not root: return []
        if root and not root.left and not root.right:
            if root.val == s:
                return [[s]]
            else:
                return []
        res = []
        def _helper(root, path):
            if not root: return
            if root and not root.left and not root.right:
                path.append(root.val)
                res.append(path)
            if root.left:
                _helper(root.left, path + [root.val])
            if root.right:
                _helper(root.right, path + [root.val])
        _helper(root, [])
        return [i for i in res if sum(i) == s]

if __name__ == '__main__':
    l = TreeNode(5)
    l.left = TreeNode(4)
    l.right = TreeNode(8)
    l.left.left = TreeNode(11)
    l.right.left = TreeNode(13)
    l.right.right = TreeNode(4)
    l.left.left.left = TreeNode(7)
    l.left.left.right = TreeNode(2)
    l.right.right.left = TreeNode(5)
    l.right.right.right = TreeNode(1)
    print(l.pathSum(l, 22))
    print(l.pathSum_stupid(l, 22))
       
            
            