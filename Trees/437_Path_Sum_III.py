from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    def pathSum(self, root, s):  # O(n) both
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return 
            # current prefix sum
            curr_sum += node.val
            # here is the sum we're looking for
            if curr_sum == k:
                count += 1
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            count += h[curr_sum - k]
            # add the current sum into hashmap
            # to use it during the child nodes processing
            h[curr_sum] += 1
            # process left subtree
            preorder(node.left, curr_sum)
            # process right subtree
            preorder(node.right, curr_sum) 
            # remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            h[curr_sum] -= 1
        count, k = 0, s
        h = defaultdict(int)
        preorder(root, 0)
        return count


    def pathSum_stack(self, root, s):
        if not root:
            return 0
        # save (node, accumulated_sum) into stack
        stack = [(root, root.val)]
        res = 0
        visited_left, visited_right = [], []
        sum_map = defaultdict(int)
        sum_map[root.val] = 1
        while stack:
            node, acum = stack[-1]
            while node.left and node.left not in visited_left:
                stack.append((node.left, acum + node.left.val))
                sum_map[acum + node.left.val] += 1
                visited_left.append(node.left)
                
                acum += node.left.val
                node = node.left
                
            if node.right and node.right not in visited_right:
                stack.append((node.right, acum + node.right.val))
                sum_map[acum+node.right.val] += 1
                visited_right.append(node.right)
            
            else:
                node, acum = stack.pop()
                sum_map[acum] -= 1
                # target sum starts from the beginning of the array
                if acum == s:
                    res += 1
                # target sum starts somewhere in the middle.
                res += sum_map[acum - s]
        return res


    def pathSum_short(self, root, s):
        def dfs(node: TreeNode, sums: List[int]) -> int:
            if not node:
                return 0
            sums = [s + node.val for s in sums] + [node.val]
            res = sums.count(s)
            res += dfs(node.left, sums) if node.left else 0
            res += dfs(node.right, sums) if node.right else 0
            return res
        return dfs(root, [])