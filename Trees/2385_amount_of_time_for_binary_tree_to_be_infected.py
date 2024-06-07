# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
    def amountOfTime_dfs(self, root, start):  # O(n) both
        """
        it's a DFS in which we recursively build a tree
        and process it
        """
        adj_d = defaultdict(list)
        def _buildTree(node):
            """
            helper to build a dict that looks like
            d[node] = [children]
            """
            if node is None:
                return
            if node.left:
                adj_d[node.val].append(node.left.val)
                adj_d[node.left.val].append(node.val)
                _buildTree(node.left)
            if node.right:
                adj_d[node.val].append(node.right.val)
                adj_d[node.right.val].append(node.val)
                _buildTree(node.right)
        
        _buildTree(root)
        q, seen, res = deque(), set(), 0
        q.append(start)
        seen.add(start)
        while q:
            curr_size = len(q)
            while curr_size:
                curr_node = q.popleft()
                seen.add(curr_node)
                for element in adj_d[curr_node]:
                    if element not in seen:
                        q.append(element)
                curr_size -= 1
            res += 1
        return res - 1

    def amountOfTime_graph(self, root, start):  # O(n) both
        adj_d = defaultdict(list)
        # helper to build a dict node: [children]. It contains values, not nodes!
        def _helper(curr_node, parent):
            if curr_node and parent:
                adj_d[curr_node.val].append(parent.val)
                adj_d[parent.val].append(curr_node.val)
            if curr_node.left:
                _helper(curr_node.left, curr_node)
            if curr_node.right:
                _helper(curr_node.right, curr_node)
        
        _helper(root, 0)
        seen = set()
        q = deque()
        q.append((start, 0))
        while q:
            curr_node, curr_time = q.popleft()
            seen.add(curr_node)
            for neigh in adj_d[curr_node]:
                if neigh not in seen:
                    q.append((neigh, curr_time + 1))
        return curr_time

  
        