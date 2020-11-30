from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def findLeaves(self, root):  # doesn't work for edge cases 
        res = []
        def _helper_height(node):
            if not node: return 0
            if node and not node.left and not node.right: return 1
            l = _helper_height(node.left)
            r = _helper_height(node.right)
            return max(l, r) + 1
        d = defaultdict(list)
        # traversed = []
        def _trav(node, traversed):
            if not node: return
            traversed.append(node)
            _trav(node.left, traversed)
            _trav(node.right, traversed)
            return traversed
        traversed = _trav(root, [])
        for item in traversed:
            d[_helper_height(item)].append(item.val)
        return [v for v in d.values()][::-1]


    def findLeaves_alt(self, root):
        res = []
        def helper(node):
		    # When we read the leaf return -1 (to help start our levels at 0 - because we add 1 when returned).
            if not node:
                return -1
			# find the height of the l and r subtrees.
            left = helper(node.left)
            right = helper(node.right)
			# We have to take the max height given that we're pruning, eg. must maintain our root
			# as being the max height if our tree is unbalanced (or depths aren't equal).
            level = max(left, right) + 1
			# If we haven't visited a level, append to the results.
            if len(res) <= level:
                res.append([])
			# Append node value at its given level.
            res[level].append(node.val),
            return level       
        helper(root)
        return res

if __name__ == '__main__':
    l = TreeNode(1)
    l.left = TreeNode(2)
    l.right = TreeNode(3)
    l.left.left = TreeNode(4)
    l.left.right = TreeNode(5)
    # print(l.test_traversed(l, []))
    print(l.findLeaves(l))
    print(l.findLeaves_alt(l))