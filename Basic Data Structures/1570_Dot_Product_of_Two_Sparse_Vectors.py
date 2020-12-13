class SparseVector:
    def __init__(self, nums):
        # self.nums = nums
        self.d = {}
        for k, v in enumerate(nums):
            if v != 0:
                self.d[k] = v
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        res = 0
        for k, v in self.d.items():
            if k in vec.d:
                res += v * vec.d[k]
        return res