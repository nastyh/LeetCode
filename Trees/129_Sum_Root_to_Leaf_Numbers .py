# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def sumNumbers(self, root):
        ans = 0
        res = []

        def _helper(root, paths):
            if not root: return []
            if not root.left and not root.right:
                res.append(paths)
            else:
                if root.left: _helper(root.left, paths + [root.left.val])
                if root.right: _helper(root.right, paths + [root.right.val])
            return res

        vals = _helper(root, [root.val]) if root else None
        if vals:
            for l in vals:
                curr_val = int(''.join([str(i) for i in l]))
                ans += curr_val
        return ans


    # def sumNumbers_BFS(self, root):
def test(nums):
    ans = 0
    for i in range(len(nums)):
        ans += list(reversed(nums))[i] * 10**i
    return ans


if __name__ == '__main__':
    l = TreeNode(4)
    l.left = TreeNode(9)
    l.right = TreeNode(0)
    l.left.left = TreeNode(5)
    l.left.right = TreeNode(1)
    print(l.sumNumbers(l))
    m = TreeNode(1)
    m.left = TreeNode(2)
    m.right = TreeNode(3)
    print(m.sumNumbers(m))
    # print(test([4,9,5]))
