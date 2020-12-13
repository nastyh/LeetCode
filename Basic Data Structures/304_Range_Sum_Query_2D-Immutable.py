class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        rl, cl = len(matrix), len(matrix[0])
        self.m = [[0 for _ in range(cl + 1)] for _ in range(rl + 1)]
        for i in range(1, rl + 1):
            for j in range(1, cl + 1):
                self.m[i][j] = matrix[i - 1][j - 1] + self.m[i - 1][j] + self.m[i][j - 1] - self.m[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.m[row2][col2] - self.m[row2][col1 - 1] - self.m[row1 - 1][col2] + self.m[row1 - 1][col1 - 1]


class NumMatrix:  # intersections. 
    """
    what we are looking is everything minus the rectangle above minus the rectangle to the left
    """

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]: return None
        row = len(matrix)
        col = len(matrix[0])
        self.dp = [[0]*(col + 1) for _ in range(row + 1)]
        for i in range(1,row + 1):
            for j in range(1,col + 1):
                self.dp[i][j]=self.dp[i][j - 1]+self.dp[i - 1][j]-self.dp[i - 1][j - 1]+matrix[i - 1][j - 1]
				
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1]-self.dp[row2 + 1][col1]-self.dp[row1][col2 + 1]+self.dp[row1][col1]