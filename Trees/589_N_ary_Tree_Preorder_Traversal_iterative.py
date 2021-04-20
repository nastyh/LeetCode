class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def preorder(self, root):  # O(N) both 
        res, s = [], []
        if not root:
            return None
        s.append(root)
        while s:
            t = s.pop()
            if t:
                res.append(t.val)
                for i in range(len(t.children) -1, -1, -1):
                    s.append(t.children[i])
        return res


    def preorder_iter_clean(self, root):
        """
        Put the root into the stack. Pop. Put its children in an opposite order b/c we need to traverse from the bottom
        """
        st, res = [], []
        if not root: return
        st.append(root)
        while st:
            t = st.pop()
            res.append(t.val)
            for child in t.children[::-1]:
                st.append(child)
        return res 
        
    
    def preorder_recur(self, root):
        """
        Traditional recursive pre-order but just treat children in a for loop
        """
        res = []
        def _helper(node):
            if not node: return
            res.append(node.val)
            for child in node.children:
                _helper(child)        
        _helper(root)
        return res
