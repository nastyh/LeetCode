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
            # curr_level, curr_avg, nodes_in_level = 0, 0, 0
            curr_level, nodes_in_level = 0, 0
            for _ in range(len(d)):
                t = d.popleft()
                curr_level += t.val
                nodes_in_level += 1
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
                # curr_avg = curr_level / nodes_in_level
            res.append(curr_level / nodes_in_level)
        return res

    
    def averageOfLevels_most_precise(self, root):  # O(h) and O(1)
        if not root: return [0]
        if root and not root.left and not root.right: return [root.val]
        d, res = deque(), []
        d.append(root)
        while d:
            level_size, curr_sum = len(d), 0
            for _ in range(len(d)):
                t = d.popleft()
                curr_sum += t.val
                if t.left:
                    d.append(t.left)
                if t.right:
                    d.append(t.right)
            res.append(curr_sum / level_size)
        return res


    def averageOfLevels_dfs(self,root):
        if root is not None:
            output = []
            depth = 0

            def trav(node, depth):
                depth += 1
                if len(output) < depth:
                    output.append([])
                output[depth - 1].append(node.val)
                if node.left is not None:
                    trav(node.left, depth)
                if node.right is not None:
                    trav(node.right, depth)

            trav(root, depth)
            return [sum(x)/len(x) for x in output]
        else:
            return []

if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(9)
    l.right = TreeNode(20)
    l.right.left = TreeNode(15)
    l.right.right = TreeNode(7)
    print(l.averageOfLevels(l))
    print(l.averageOfLevels_dfs(l))
