class NumMatrix:  # best

    def __init__(self, matrix: List[List[int]]):
        """
        dp is a matrix where rows are the running sum of the rows in matrix
        first column is always the same, cumulative sum starts with the second element
        """
        self.matrix = matrix
        self.dp = [[0] * len(self.matrix[0]) for _ in range(len(self.matrix))]
        for row in range(len(self.matrix)):
            self.dp[row][0] = self.matrix[row][0]
        for row in range(len(self.matrix)):
            for col in range(1, len(self.matrix[0])):
                self.dp[row][col] = self.dp[row][col - 1] + self.matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        formula for every row: dp[right] - dp[left] + matrix[left]
        need a for loop to cover the required rows 
        """
        res = 0
        for i in range(0, row2 - row1 + 1):
            res += self.dp[row1 + i][col2] - self.dp[row1 + i][col1] + self.matrix[row1 + i][col1] 
        return res
        

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

    def __init__(self, matrix):
        if not matrix or not matrix[0]: return None
        row = len(matrix)
        col = len(matrix[0])
        self.dp = [[0]*(col + 1) for _ in range(row + 1)]
        for i in range(1,row + 1):
            for j in range(1,col + 1):
                self.dp[i][j]=self.dp[i][j - 1]+self.dp[i - 1][j]-self.dp[i - 1][j - 1]+matrix[i - 1][j - 1]
				
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1]-self.dp[row2 + 1][col1]-self.dp[row1][col2 + 1]+self.dp[row1][col1]


def test(matrix, row1, col1, row2, col2):
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        dp[row][0] = matrix[row][0]
    for row in range(len(matrix)):
        for col in range(1, len(matrix[0])):
            dp[row][col] = dp[row][col - 1] + matrix[row][col]
    # print(dp)
    res = 0
    # print(matrix)
    # print(dp)
    for i in range(0, row2 - row1 + 1):
        res += dp[row1 + i][col2] - dp[row1 + i][col1] + matrix[row1 + i][col1] 
        # print(res, matrix[row1 + i][col1] )
        # res += matrix[row1 + i][col1] 
        
    return res
    # pass
mtx =  [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
if __name__ == '__main__':
    print(test(mtx, 2, 1, 4, 3))
    print(test(mtx, 1, 1, 2, 2))
    print(test(mtx, 1, 2, 2, 4))