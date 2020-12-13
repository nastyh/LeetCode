# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def getMinimumDifference(self, root):
        values_list = []
        def get_values(node):  # inorder traversal; returns a sorted array
            if not node: return 
            get_values(node.left)
            values_list.append(node.val)
            get_values(node.right)

        # def get_values_bfs(root): # same as above, but BFS
        #     d = deque()
        #     values = []
        #     d.append(root)
        #     while d:
        #         t = d.popleft()
        #         values.append(t.val)
        #         if t.left:
        #             d.append(t.left)
        #         if t.right:
        #             d.append(t.right)
        #     return values

        get_values(root)
        # values_list = get_values_bfs(root)

        if len(values_list) != len(set(values_list)):
            return 0
        minimum_diff = values_list[1] - values_list[0]

        for i in range(1, len(values_list)):
            diff = values_list[i] - values_list[i - 1]
            if diff < minimum_diff:
                minimum_diff = diff
        return minimum_diff

if __name__ == '__main__':
    l = TreeNode(1)
    l.right = TreeNode(3)
    l.right.left = TreeNode(2)
    print(l.getMinimumDifference(l))
