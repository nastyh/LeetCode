# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  # O(n) hopefully both
        """
        idea is to have a dictionary like
        number_of_column: [list of values at this column]
        then we need to go over the sorted dictionary and collect
        the values into one big list 
        """
        # two edge cases
        if not root: return None
        if root and not root.left and not root.right: return [[root.val]]
        q, d_col = deque(), defaultdict(list)
        q.append([root, 1]) # assume the root is in column 1
        while q:
            curr_n, curr_col = q.popleft()
            d_col[curr_col].append(curr_n.val)  # keep building our dictionary
            if curr_n.left:
                q.append([curr_n.left, curr_col - 1])
            if curr_n.right:
                q.append([curr_n.right, curr_col + 1])
        # return a list of lists 
        return [v for k, v in sorted(d_col.items())]

    def verticalOrder_another(self, root: Optional[TreeNode]) -> List[List[int]]:  # O(n) hopefully both
        """
        Twist: know the index of the most left column
        and the index of the most right column
        It can help at the end: we won't need to sort the dictionary
        but rather run a for loop from the smallest to the largest index
        """
         # two edge cases
        if not root: return None
        if root and not root.left and not root.right: return [[root.val]]
        q, d_col = deque(), defaultdict(list)
        most_left_col_ix = most_right_col_ix = 1
        res = []
        q.append([root, 1]) # assume the root is in column 1
        while q:
            curr_n, curr_col = q.popleft()
            most_left_col_ix = min(most_left_col_ix, curr_col)
            most_right_col_ix = max(most_right_col_ix, curr_col)
            d_col[curr_col].append(curr_n.val)  # keep building our dictionary
            if curr_n.left:
                q.append([curr_n.left, curr_col - 1])
            if curr_n.right:
                q.append([curr_n.right, curr_col + 1])
        # this is where we use col indices, since the most left one is the smallest
        # the most right one is the largest
        for i in range(most_left_col_ix, most_right_col_ix + 1):
            res.append(d_col[i])
        return res