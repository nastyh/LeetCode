# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # O(n) both
        d = {}
        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                value = left + '-' + right + '-' + str(node.val)
                if value in d:
                    d[value].append(node)
                else:
                    d[value] = [node]
                return value
            else:
                return 'N'
        dfs(root)
        ans = []
         for i in d:
            if len(d[i]) >= 2:
                ans.append(d[i][0])
        return ans

    def findDuplicateSubtrees_preorder(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        preorder traversal of the binary tree and serialize each subtree into a string.
        We can then store the serialized string in a hash table and check if we have seen it before.
        If we have seen it before, it means that the subtree is a duplicate and we can add it to the result list.
        O(n) both 
        """
        result = []
        cache = {}

        def traverse(result, cache, root):
            if not root:
                return ""

            left = traverse(result, cache, root.left)
            right = traverse(result, cache, root.right)
            current = str(root.val) + "$" + left + "$" + right

            if current not in cache:
                cache[current] = 0 
            elif cache[current] == 1:
                result.append(root)

            cache[current] += 1

            return current

        traverse(result, cache, root)
        return result

    