# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
        # if (root.left.val == p.val and root.right.val == q.val) or (root.left.val == q.val and root.right.val = p.val):
            return root


"""
If we have parent pointers for each node we can traverse back from p and q to get their ancestors. The first common node we get during this traversal would be the LCA node. We can save the parent pointers in a dictionary as we traverse the tree.

Algorithm

Start from the root node and traverse the tree.
Until we find p and q both, keep storing the parent pointers in a dictionary.
Once we have found both p and q, we get all the ancestors for p using the parent dictionary and add to a set called ancestors.
Similarly, we traverse through ancestors for node q. If the ancestor is present in the ancestors set for p, this means this is the first ancestor common between p and q (while traversing upwards) and hence this is the LCA node."""
    def lca(root):
        if not root:
            return 0
        if root.val == p.val or root.val == q.val:
            return root
        left = lca(root.left)
        right = lca(root.right)
        if not left and not right:
            return 0
        if left and right:
            return root
        return left if left else right
        return lca(root)

     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        stack = [root]
        parent = {root:None}
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
                parent[cur.right] = cur
            if cur.left:
                stack.append(cur.left)
                parent[cur.left] = cur
            if p in parent and q in parent:
                break
        # print(parent)
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q


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


