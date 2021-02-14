def lowestCommonAncestor(self, root, nodes):
    if root == None:
        return None
    if root in nodes:
        return root
    left =  self.lowestCommonAncestor(root.left, nodes)
    right = self.lowestCommonAncestor(root.right, nodes)
    if right == None:
        return left
    elif left == None:
        return right
    else:
        return root