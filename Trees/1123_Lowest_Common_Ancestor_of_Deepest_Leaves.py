# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def lcaDeepestLeaves(self, root):  # O(n) and O(n) in the worst case, but on average O(log(n))
        def helper(node):
            if not node:
                return [node, 0]
            if not node.left and not node.right:
                return [node, 0]

            if not node.right:
                left_node, left_dep = helper(node.left)
                return [left_node, left_dep + 1]

            if not node.left:
                right_node, right_dep = helper(node.right)
                return [right_node, right_dep + 1]

            left_node, left_dep = helper(node.left)
            right_node, right_dep = helper(node.right)
            if left_dep > right_dep:
                return [left_node, left_dep + 1]
            elif left_dep < right_dep:
                return [right_node, right_dep + 1]
            else:
                return [node, left_dep + 1]

        return helper(root)[0]

        # easier to understand

    def lcaDeepestLeaves_easy(self, root):
        def _helper(node):
            if not node:
                return (None, 0)
            l_node, l_depth = _helper(node.left)
            r_node, r_depth = _helper(node.right)

            if l_depth == r_depth:
                return (node, l_depth + 1)
            elif l_depth > r_depth:
                return (l_node, l_depth + 1)
            else:
                return (r_node, r_depth + 1)
        n, d = _helper(root)
        return n

    def lcaDeepestLeaves_bfs_another(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        O(n) both 
        traverse level by level and have a dict shaped as node: its parent 
        collect each level into level_nodes and rewrite it for each level
        at the end, level_nodes will contain the deepest/last level 
        than go through these results, reference the dict and extract a parent for each
        node from the deepest level. 
        """
        if not root: return []
        parent = {root: None}
        q = deque([root])
        deepest = []
        while q:
            level_nodes = []
            for _ in range(len(q)):
                node = q.popleft()
                level_nodes.append(node)
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)
            deepest = level_nodes 
            nodes = deepest
            while len(nodes) > 1:
                nodes = list({parent[node] for node in nodes})
        return nodes[0]



if __name__ == '__main__':
    l = TreeNode(11)
    l.left = TreeNode(4)
    l.right = TreeNode(16)
    l.left.left = TreeNode(2)
    l.left.right = TreeNode(8)
    l.left.right.left = TreeNode(6)
    l.left.right.right = TreeNode(10)
    print(l.lcaDeepestLeaves_easy(l))
