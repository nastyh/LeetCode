from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def top_view(root):
    """
    O(nlogn) due to sorting the n nodes -- worst. Best: O(n) if k << n. k is the num of levels
    O(n) due to the deque 
    need to track a horizontal distance from the root, which is 0
    left child is parent horizontal - 1, the right: parent horizontal + 1
    deque as always
    dicto to map the horizontal distance to the first node encountered in this particular level
    """
    if not root:
        return []
    # Dictionary to store the first node at each horizontal distance
    top_view_map = {} # {level: the left node at this level}
    # Queue for BFS: stores pairs of (node, horizontal_distance)
    queue = deque([(root, 0)]) # root is zero horizontal distance
    while queue:
        node, hd = queue.popleft() # node and the horizontal distance
        # If the HD is not already in the map, add it
        if hd not in top_view_map:
            top_view_map[hd] = node.val
        # Traverse left and right children with updated HD
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    # Extract the top view from the map (sorted by HD)
    # it's sorted from the smallest hd value (the most top left node, meaning it's the widest level)
    # to the the largest hd value (meaning it's the most top right node )
    return [top_view_map[hd] for hd in sorted(top_view_map)]

# Example usage:
# Construct the first tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(6)
root1.right.left.left = TreeNode(7)
root1.right.left.right = TreeNode(8)

print(top_view(root1))  # Output: [2, 1, 3, 6]

# Construct the second tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.left.right.right = TreeNode(5)

print(top_view(root2))  # Output: [2, 1, 3]
