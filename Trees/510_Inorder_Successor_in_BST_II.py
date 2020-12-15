# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def inorderSuccessor(self, node):  # O(logn n), O(1)
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node == node.parent.right:
        node = node.parent
    return node.parent
