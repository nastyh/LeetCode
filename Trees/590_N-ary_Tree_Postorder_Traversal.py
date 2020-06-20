
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def postorder(self, root):
    	if root is None:
            return []
        
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
                
        return output[::-1]

    def postorder_recurs(self, root):
    	 def _helper(root, res):
            if root is None:
                return res
            for c in root.children:
                _helper(c, res)
            res.append(root.val)
            return res
        return _helper(root, [])