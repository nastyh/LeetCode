# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def rightSideView_efficient(self, root): # bit less space than the variant below, b/c it doesn't save everything in res. Space complexity is probably O(d), where d
    # is a diameter of a tree
        if not root: return []
        res = []
        d = deque()
        d.append(root)
        while d:
            curr = []
            for _ in range(len(d)):
                t = d.popleft()
                curr.append(t.val)
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            res.append(curr[-1])
        return res

    def rightSideView(self, root): # bfs
        from collections import deque
        res = []
        if not root:
            return []
        q = deque()
        q.append(root)

        while q:
            curr_level = []
            for _ in range(len(q)):
                t = q.popleft()
                curr_level.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            res.append(curr_level)
        return [i[-1] for i in res]


    def rightSideView_rec(self, root): # a bit different approach
        if not root:
            return []
        ans = []
        max_height = [-1] #I am defining this as a list to be able to change it in the recursive calls of helper
        self.helper(root, 0, max_height, ans)
        return ans

    def helper(self, node, cur_height, max_height, ans):
        if not node:
            return
        if cur_height > max_height[0]:
            ans.append(node.val)
            max_height[0] = cur_height

        self.helper(node.right, cur_height+1, max_height, ans)
        self.helper(node.left, cur_height+1, max_height, ans)


if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.right = TreeNode(5)
    l.right.right = TreeNode(4)
    print(l.rightSideView_efficient(l))
    print(l.rightSideView(l))
    print(l.rightSideView_rec(l))


