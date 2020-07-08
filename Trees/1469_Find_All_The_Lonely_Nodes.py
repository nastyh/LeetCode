class TreeNode:
	def __init__(self, val=0, left=None, right=None):
	    self.val = val
	    self.left = left
	    self.right = right

	def getLonelyNodes_short(self, root):
		res = []
		
		def _helper(root):
			if not root:return []
			if root and not root.left and not root.right:
				return res
			if root and root.left and not root.right:
				res.append(root.left.val)
			if root and not root.left and root.right:
				res.append(root.right.val)
			l = _helper(root.left)
			r = _helper(root.right)
			if l: return l
			if r: return r 
		_helper(root)
		return res 


if __name__ == '__main__':
	l = TreeNode(1)
	l.left = TreeNode(2)
	l.right = TreeNode(3)
	l.left.right = TreeNode(4)
	m = TreeNode(7)
	m.left = TreeNode(1)
	m.right = TreeNode(4)
	m.left.left = TreeNode(6)
	m.right.left = TreeNode(5)
	m.right.right = TreeNode(3)
	m.right.right.right = TreeNode(2)
	print(l.getLonelyNodes_short(l))
	print(m.getLonelyNodes_short(m))


  