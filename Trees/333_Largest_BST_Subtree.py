class Solution:
    def largestBSTSubtree(self, root):
        ans = 0
        def isBSTandCount(r):  
            nonlocal ans
            if not r: return True, 0, math.inf, -math.inf
            isl, lCount, lMin, lMax = isBSTandCount(r.left)
            isr, rCount, rMin, rMax = isBSTandCount(r.right)
            if isl and isr and lMax < r.val and rMin > r.val: 
                self.ans = max(self.ans, lCount + rCount + 1)
                return True, lCount + rCount + 1, min(lMin, r.val), max(rMax, r.val)
            else:
                return False, 0, 0, 0
        _,_,_,_ = isBSTandCount(root)
        return ans
