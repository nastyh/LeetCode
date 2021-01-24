def minDistance_dp(word1, word2):  # O(mn) both 
    """
    dp is a matrix of word1 + 1 and word2 + 1 sizes
    first row means that len(word1) is equal to zero. To make word2 equal to zero, we need to remove as many elements as in len(word2). Thus, we can fill out the first row
    The same logic applies to the first col. But here we're trying to make word1 equal to zero
    When we move along the rows/cols, it means that we're considering longer strings
    Then start filling out from the cell (1, 1)
    Insert operation: res(m, n) = res(m, n - 1) + 1. Moving horizontally
    Remove operation: res(m, n) = res(m - 1, n) + 1. Moving vertically
    Replace operation: res(m, n) = res(m - 1, n - 1) + 1. Moving diagonally
    Always choose the min of the three and fill out the table. 
    """
    dp = [[None] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for col in range(len(word2) + 1):
        dp[0][col] = col
    for row in range(len(word1) + 1):
        dp[row][0] = row
    for row in range(1, len(word1) + 1):
        for col in range(1, len(word2) + 1):
            if word1[row - 1] == word2[col - 1]:  # if the latest chars are the same ignore them and process the rest
                dp[row][col] = dp[row - 1][col - 1]
            else:
                _insert = dp[row][col - 1]
                _remove = dp[row - 1][col]
                _replace = dp[row - 1][col - 1]
                dp[row][col] = 1 + min(_insert, _remove, _replace)
    return dp[-1][-1]


def minDistance_dp_optimized(word1, word2): # O(mn) and O(2n) where n is the length of word2
    dp = [[0 for i in range(len(word2) + 1)] for j in range(2)]
    for i in range(len(word2) + 1):
        dp[0][i] = i
    for i in range(1, len(word1) + 1):
        dp[i%2][0] = i;
        for j in range(1, len(word2) + 1):
            cost = 1 if word1[i - 1] != word2[j - 1] else 0;
            dp[i%2][j] = min(dp[(i - 1) % 2][j - 1] + cost, dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1)
    return dp[len(word1) % 2][len(word2)]


def minDistance(word1, word2):  # O(mn) and O(2n) where n is the length of word2
    if len(word2) > len(word1):
        return self.minDistance(word2, word1)
    evenRow = [i for i in range(len(word2) + 1)]
    oddRow = [0 for i in range(len(word2) + 1)]
    currentRow = evenRow
    for i in range(1, len(word1) + 1):
        if (i % 2) == 0:
            currentRow = evenRow
            prevRow = oddRow
        else:
            currentRow = oddRow
            prevRow = evenRow
        for j in range(len(word2) + 1):
            if j == 0:
                currentRow[0] = prevRow[0] + 1
            elif word1[i - 1] == word2[j - 1]:
                currentRow[j] = prevRow[j - 1]
            else:
                currentRow[j] = min(currentRow[j - 1], prevRow[j], prevRow[j - 1]) + 1
    return currentRow[-1]


if __name__ == '__main__':
    print(minDistance_dp('horse', 'ros'))
    print(minDistance_dp('intention', 'execution'))
    print(minDistance_dp_optimized('horse', 'ros'))
    print(minDistance_dp_optimized('intention', 'execution'))
