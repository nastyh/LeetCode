class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def findPredcessor(self, root, elToFind): # elToFind is given as a root, I guess
        res = None
        if not root:
            return
        if elToFind.left:
            t = elToFind.left
            while t.right:
                t = t.right
            res = t.val
        else:
            while elToFind.val != root.val:
                if elToFind.val > root.val:
                    t1 = root
                    root = root.right
                else:
                    root = root.left
            try:
                res = t1.val
            except UnboundLocalError:
                return None
        return res


    def findPred_rec(self, root, elToFind):
        res = 0
        if not root: return
        if root.val == elToFind.val:
            if root.left:
                t = root.left
                while t:
                    t = t.left
                res = t.val
            else:
                if elToFind.val < root.val:
                    res = root.val
                    findPred_rec(root.left, elToFind)
                else:
                    res = root.val
                    findPred_rec(root.right, elToFind)

        return res

if __name__ == '__main__':
    l = TreeNode(50)
    l.left = TreeNode(16)
    l.right = TreeNode(90)
    l.left.left = TreeNode(14)
    l.left.right = TreeNode(40)
    l.right.left = TreeNode(78)
    l.right.right = TreeNode(100)
    f = l.left.left

print(l.findPredcessor(l, f))
# print(l.findPred_rec(l, f))
