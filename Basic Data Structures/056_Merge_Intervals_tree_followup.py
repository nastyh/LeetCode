class TreeNode:
    def __init__(self, start, end, middle):
        self.start = start
        self.end = end
        self.middle = middle
        self.left = self.right = None

class Solution:
    def __init__(self):
        self.root = None
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        for start, end in intervals:
            if not self.root:
                self.root = TreeNode(start, end, (start + end) // 2)
            else:
                self.add(self.root, start, end)
        
        return self.query(self.root)
    
    
    def add(self, node, start, end):     
        if end < node.middle:
            if node.left:
                self.add(node.left, start, end)
            else:
                node.left = TreeNode(start, end, (start + end) // 2)
        
        elif start > node.middle:
            if node.right:
                self.add(node.right, start, end)
            else:
                node.right = TreeNode(start, end, (start + end) // 2)
        
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)
    
    def query(self, node):
        if not node:
            return []
        
        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []
        
        inserted = False
        
        for lres in left_intervals:
            if lres[1] < node.start:
                res.append(lres)
            else:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break
        
        if not inserted:
            res.append([node.start, node.end])
        
        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)
        
        return res