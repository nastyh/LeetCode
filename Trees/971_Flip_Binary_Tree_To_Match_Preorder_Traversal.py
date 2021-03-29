def flipMatchVoyage(self, root, voyage):  # O(N) both 
    """
    navigate the binary tree from the root in a pre-order traversal and compare the node values with the values in the voyage array (V)
    In dfs()  take care of the exit conditions when the recursive function reaches a null node or when we've already found a failure.
    Then, if the node value is not the one expected, we should set our answer to [-1].
    We can simply check the left node value against the next index of V, and if they're not a match, we should account for the flip by updating ans.
    Rather than actually flipping around nodes in the binary tree, however, we can simply simulate the flip by recursing the two branches in reverse order.
    Otherwise, we can proceed with normal pre-order traversal.
    """
    ans = [0]
    def dfs(node, V, ans):
        if not node or ans[0] == -1: return
        if node.val != V[ans[0]]: ans[0] = -1
        else:
            ans[0] += 1
            if node.left and node.left.val != V[ans[0]]:
                ans.append(node.val)
                dfs(node.right, V, ans)
                dfs(node.left, V, ans)
            else:
                dfs(node.left, V, ans)
                dfs(node.right, V, ans)
    dfs(root, V, ans)
    return ans[:1] if ans[0] == -1 else ans[1:]


def flipMatchVoyage_another(self, root, voyage):
    """
    starting at each node by checking if the value matches the next expected value in voyage
    before adding the child nodes to the stack the left node is checked as a potential match to the next value in voyage.
    If the left node does not match, the child nodes are flipped and the traversal continues.
    """
    flips = []       # list of values for flipped nodes
    i = 0            # index for value in voyage to match next
    # Perform a pre-order traversal, swapping nodes if needed
    nodes = [root]
    while nodes:
        node = nodes.pop()
        if node.val != voyage[i]: # Tree can't be made to match voyage
            return [-1]
        i += 1  # node matched so we advance to the next in voyage
        # Flip if the left node doesn't match the next value in voyage
        if node.left and node.left.val != voyage[i]:
            node.left, node.right = node.right, node.left
            flips.append(node.val)
        # Continue the pre-order traversal
        if node.right:
            nodes.append(node.right)
        if node.left:
            nodes.append(node.left)
    return flips    