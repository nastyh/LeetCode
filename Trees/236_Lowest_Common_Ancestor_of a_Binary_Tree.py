# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        if l:
            return l
        if r:
            return r
        return None


    # super slow but straightfoward: create two lists with paths to p and q. The last common element is what we need to return
    def lowestCommonAncestor_alt(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        def _path2Node(node, node_to_find, path):
            if not node:
                return []
            if node.val == node_to_find.val:
                path.append(node_to_find)
                return path
            l = _path2Node(node.left, node_to_find, path + [node])
            r = _path2Node(node.right, node_to_find, path + [node])
            if l:
                return l
            if r:
                return r


        p_path = _path2Node(root, p, [])
        q_path = _path2Node(root, q, [])

        if len(p_path) <= len(q_path):
            longer = q_path
            shorter = p_path
        else:
            longer = p_path
            shorter = q_path

        matching = [x for x in longer if x in shorter]
        return matching[-1]




if __name__ == '__main__':
    l = TreeNode(3)
    l.left = TreeNode(5)
    l.right = TreeNode(1)
    l.left.left = TreeNode(6)
    l.left.right = TreeNode(2)
    l.left.right.left = TreeNode(7)
    l.left.right.right = TreeNode(4)
    l.right.left = TreeNode(0)
    l.right.right = TreeNode(8)

    print(l.lowestCommonAncestor(l, l.left, l.right)) # returns 3
    print(l.lowestCommonAncestor_alt(l, l.left, l.right))


