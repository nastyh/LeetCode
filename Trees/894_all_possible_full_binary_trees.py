# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT_recursive(self, n: int) -> List[Optional[TreeNode]]:
        """
        full binary tree:
        all the nodes have either 0 or 2 children 
        complete binary tree:
        all have the max number of children and as left as possible

        starting from the root node using combinatorial search recursively and backtracking.
        O(2^n) b/c of the combinations
        O(n^2) highest levels is a factor of n
        """
        res = []
        if not n % 2: # impossible to produce even num full tree
            return res
        def generate_trees(n, node, unprocessed):
            if n == 0:
                res.append(deepcopy(head))
                return
            node.left = TreeNode()
            node.right = TreeNode()
            unprocessed.append(node.left)
            unprocessed.append(node.right)
            # go over every combination of dfs expansion based on unprocessed candidates
            for ix, next_node in enumerate(unprocessed):
                generate_trees(n - 2, next_node, unprocessed[ix + 1:])
                next_node.left = next_node.right = None # backtrack
                if n - 2 == 0: return # don't double count dups
        head = TreeNode()
        unprocessed = []
        generate_trees(n - 1, head, unprocessed)
        return res  

    @cache
    def allPossibleFBT_recursive_another(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2:
            return []
        elif n == 1:
            return [TreeNode(0)]
        else:
            return [
                TreeNode(0, left=lt, right=rt)
                for i in range(1, n, 2)
                for lt in self.allPossibleFBT(i)
                for rt in self.allPossibleFBT(n - 1 - i)]
        
