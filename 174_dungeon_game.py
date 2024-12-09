class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        O(mn) both
        dp the same size as dungeon
        when we arrive to the last cell we need to have enough health points so that
        (what we have + value in the last cell) >=1 
        Each cell contains a value of health we need in order to arrive to this cell, get a potential hit and survive
        So we will work our dp from the end
        dp[i][j] = max(1, prev_cell_best_value - dungeon[i][j])
        possible cases:
        can't get to this point by traversing the array
        can get to point in one way
         can get to point by two ways (choose the path with the min value)
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))] 
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1]) # last cell if it's -5, = max(1, 1-(-5))= max(1, 6) = 6 
        for i in range(m - 2, -1, -1): #2 case
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])
        for i in range(n - 2, -1, -1):    
            dp[m - 1][i] = max(1, dp[m - 1][i + 1] - dungeon[m - 1][i])
        for i in range(m - 2, -1, -1): # 3 case
            for j in range(n - 2, -1, -1):
                curr_min = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, curr_min - dungeon[i][j])
        return dp[0][0]