from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def averageOfLevels(self, root):
        d, res = deque(), []
        d.append(root)
        while d:
            curr_level, curr_avg, nodes_in_level = 0, 0, 0
            for _ in range(len(d)):
                t = d.popleft()
                curr_level += t.val
                nodes_in_level += 1
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
                curr_avg = curr_level / nodes_in_level
            res.append(curr_avg)
        return res

if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)
    print(l.averageOfLevels(l))
