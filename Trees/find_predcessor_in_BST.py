class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def findPredcessor(self, root, elToFind): # elToFind is the node which predcessor's we're looking for 
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


    def findPredcessor_alt(self, root, target):
        """
        if a target has a left child, the answer sits in the very right element of the left subtree
        If a target has a right child, start doing a binary search and choosing where to go. 
        If target > root, then go right, and keep track of prev as the last element from which you went right
        If target < root, then go left 
        Need to cover an edge case when we return a predcessor of the very first element. It's done in the second to last line 
        """
        if not root: return 
        res = None
        if target.left:
            t = target.left 
            while t.right:
                t = t.right
            return t.val
        else:
            while root.val != target.val:
                prev = None
                if target.val > root.val:
                    prev = root
                    root = root.right
                else:
                    root = root.left
                res = prev.val if prev else None
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
    o = l.right.right
    h = l

print(l.findPredcessor(l, o))
print(l.findPredcessor_alt(l, o))
# print(l.findPred_rec(l, f))
