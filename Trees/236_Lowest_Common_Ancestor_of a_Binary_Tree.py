# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def lowestCommonAncestor(self, root, p, q):  # O(n) both 
        """
        Edge case if when root is equal to p or q.
        Otherwise look for values in the lefty and right subtrees 
        """
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
    def lowestCommonAncestor_alt(self, root, p, q):
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

    
    def lowestCommonAncestor_brute_force(self, root, p, q):  # doesn't work in Leetcode but works in general
        """
        Collect two paths into two lists
        Iterate over lists: the last element before elements become different is the answer
        Edge case: [3, 5, 2, 4] and [3,5]. In this case just return the last value at which the cycle stopped 
        """
        def _path(node, to_find, curr_path):
            if not node: return []
            if node.val == to_find.val:
                curr_path.append(to_find)
                return curr_path
            l, r = None, None
            if node.left:
                l = _path(node.left, to_find, curr_path + [node])
            if node.right:
                r = _path(node.right, to_find, curr_path + [node])
            if l: return l
            if r: return r
        p_path = _path(root, p, [])
        q_path = _path(root, q, [])
        if len(p_path) == len(q_path):
            for i in range(1, len(p_path)):
                if p_path[i] != q_path[i]:
                    return p_path[i - 1]
        else: 
            i, j = 0, 0
            while i < len(p_path) and j < len(q_path):
                if p_path[i] != q_path[j]:
                    return p_path[i - 1]
                i += 1
                j += 1
            return p_path[i - 1]


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

    # print(l.lowestCommonAncestor(l, l.left, l.right)) # returns 3
    # print(l.lowestCommonAncestor_alt(l, l.left, l.right))
    print(l.lowestCommonAncestor_brute_force(l, l.left, l.right))
    print(l.lowestCommonAncestor_brute_force(l, l.left, l.left.right.right))
    print(l.lowestCommonAncestor_brute_force(l, l.left, l.left.right.right))
    print(l.lowestCommonAncestor_brute_force(l, l, l.left.right.right))



