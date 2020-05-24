class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        self._node_pos(0,0, root, d)
        return [[value[1] for value in sorted(d[key])] for key in sorted(d)]

    def _node_pos(self, X, Y, root, d):
        if not root:
            return
        d[X].append((Y, root.val))
        self._node_pos(X-1, Y+1, root.left, d)
        self._node_pos(X + 1, Y + 1, root.right, d)
