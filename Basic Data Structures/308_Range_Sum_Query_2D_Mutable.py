class NumMatrix:

    def create_prefix_sum(self, row):
        prefix_sum = []
        sum = 0
        for val in row:
            sum += val
            prefix_sum.append(sum)
        return prefix_sum
         
    def __init__(self, matrix):  # O(MN) space, M cols, N rows 
        #create this 
        self.matrix = matrix
        self.row_prefix_sum = []
        for row in matrix:
            prefix_sum = self.create_prefix_sum(row)
            self.row_prefix_sum.append(prefix_sum)
        

    def update(self, row, col, val):  # O(logN * log M)
        if row < 0 or row >= len(self.matrix):
            return 
        if col < 0 or col >= len(self.matrix[0]):
            return 
        self.matrix[row][col] = val
        #update prefix sum
        self.row_prefix_sum[row] = self.create_prefix_sum(self.matrix[row])
        

    def sumRegion(self, row1, col1, row2, col2):
        # iterate throught row1 to row2
        res = 0 
        for r in range(row1, row2 + 1):
        # calculate prefix[col2]-prefix[col1] (this sum)
            if col1==0:
                res += self.row_prefix_sum[r][col2]
            else:
                res += self.row_prefix_sum[r][col2] - self.row_prefix_sum[r][col1 - 1]
        return res



class SegmentTreeNode:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = sum

class NumMatrix:  # creating a segment tree

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.root = self.build(matrix, 0, self.m * self.n - 1)
        
    def update(self, row: int, col: int, val: int) -> None:
        index = row * self.n + col
        self.updateTree(self.root, index, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            start = i * self.n + col1
            end = i * self.n + col2
            res += self.queryTree(self.root, start, end)
        return res
        
    def build(self, A, start, end):
        if start > end:
            return None
        
        x, y = divmod(start, self.n)
        root = SegmentTreeNode(start, end, A[x][y])
        if start == end:
            return root
        
        mid = (start + end) // 2
        root.left = self.build(A, start, mid)
        root.right = self.build(A, mid + 1, end)  
        root.sum = root.left.sum + root.right.sum
        return root
    
    def updateTree(self, root, index, val):
        if not root:
            return
        
        if root.start == root.end:
            if root.start == index:
                root.sum = val
            return
        
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.updateTree(root.left, index, val)
        else:
            self.updateTree(root.right, index, val)
        root.sum = root.left.sum + root.right.sum
    
    def queryTree(self, root, start, end):
        if not root:
            return 0
        if start > root.end or end < root.start:
            return 0
        if start <= root.start and end >= root.end:
            return root.sum
        
        mid = (root.start + root.end) // 2
        res = 0
        if start <= mid:
            if end <= mid:
                lSum = self.queryTree(root.left, start, end)
            else:
                lSum = self.queryTree(root.left, start, mid)
            res += lSum
        if end > mid:
            if start > mid:
                rSum = self.queryTree(root.right, start, end)
            else:
                rSum = self.queryTree(root.right, mid + 1, end)
            res += rSum
        return res



class NumMatrix_brute_force:  # TLE but works
    """
    Create an extra dp with the running sum
    When making an update, calculate the difference between the new val and whatever is in the cell right now
    Then propagate this difference from left to right in an appropriate row in dp.
    Sum is done as usual: difference of dp elements and add back the left element from matrix
    """

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp = [[0] * len(self.matrix[0]) for _ in range(len(self.matrix))]
        for row in range(len(self.matrix)):
            self.dp[row][0] = self.matrix[row][0]
        for row in range(len(self.matrix)):
            for col in range(1, len(self.matrix[0])):
                self.dp[row][col] = self.dp[row][col - 1] + self.matrix[row][col]


    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col] 
        self.matrix[row][col] = val
        for c in range(col, len(self.dp[0])):
            self.dp[row][c] += diff
        print(self.dp)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            res += self.dp[r][col2] - self.dp[r][col1] + self.matrix[r][col1]
        # for r in range(row1, row2 + 1):
        #     for c in range(col1, col2+ 1):
        #         res += self.matrix[r][c]
        return res