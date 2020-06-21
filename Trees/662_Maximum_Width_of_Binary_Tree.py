# Definition for a binary tree node.
from collections import deque
import math
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def widthOfBinaryTree(self, root):
		if not root: return
		d, width, i, glob_width = deque(), 0, 0, -math.inf
		d.append((root, i))
		while d: 
			curr_indices = []
			for _ in range(len(d)):
				t, ix = d.popleft()
				curr_indices.append(ix)
				if t.left:
					d.append((t.left, 2 * ix))
				if t.right:
					d.append((t.right, 2 * ix + 1))
				curr_width = max(curr_indices) - min(curr_indices) + 1
			glob_width = max(glob_width, curr_width)
		return glob_width

if __name__ == '__main__':
	l = TreeNode(1)
	l.left = TreeNode(3)
	l.right = TreeNode(2)
	l.left.left = TreeNode(5)
	l.left.right = TreeNode(3)
	l.right.right = TreeNode(9)
	print(l.widthOfBinaryTree(l))
	m = TreeNode(1)
	m.left = TreeNode(3)
	m.right = TreeNode(2)
	m.left.left = TreeNode(5)
	print(m.widthOfBinaryTree(m))
	n = TreeNode(1)
	n.left = TreeNode(3)
	n.left.left = TreeNode(5)
	n.left.right = TreeNode(3)
	print(n.widthOfBinaryTree(n))
	o = TreeNode(1)
	o.left = TreeNode(3)
	o.right = TreeNode(2)
	o.left.left = TreeNode(5)
	o.right.right = TreeNode(9)
	o.left.left.left = TreeNode(6)
	o.right.right.right = TreeNode(7)
	print(o.widthOfBinaryTree(o))