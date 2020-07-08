# Definition for a binary tree node.
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def vertView(self, root):
    	if not root: return []
    	res, q, hor, d = [], deque(), 0, defaultdict(list)
    	q.append((root, hor))
    	while q:
    		t, h = q.popleft()
    		if h not in d:
    			d[h].append(t.val)
    		else:
    			d[h].append(t.val)
    		if t.left:
    			q.append((t.left, h - 1))
    		if t.right:
    			q.append((t.right, h + 1))
    	res.extend([v[-1] for k,v in sorted(d.items(), key = lambda x: x[0])])
    	return res 

if __name__ == '__main__':
	l = TreeNode(1)
	l.left = TreeNode(2)
	l.right = TreeNode(3)
	l.left.left = TreeNode(4)
	l.left.right = TreeNode(5)
	l.right.right = TreeNode(6)
	m = TreeNode(1)
	m.left = TreeNode(2)
	m.right = TreeNode(3)
	m.left.right = TreeNode(4)
	m.right.left = TreeNode(5)
	print(l.vertView(l))
	print(m.vertView(m))