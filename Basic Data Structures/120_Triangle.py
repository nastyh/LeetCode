from collections import defaultdict
def minimumTotal(triangle):
    if len(triangle) == 0:
        return 0
    if len(triangle) == 1:
        return triangle[0][0]
    dp = defaultdict(list)
    dp[0].append(triangle[0][0])
    dp[0].append(0)
    for i in range(1, len(triangle)):
        if dp[i - 1][1] == 0:
            dp[i].append(min(triangle[i][0], triangle[i][1]))
            dp[i].append(triangle[i].index(min(triangle[i][0], triangle[i][1])))
        elif dp[i - 1][1] == len(triangle[i - 1]):
            dp[i].append(min(triangle[i][-1], triangle[i][-2]))
            dp[i].append(triangle[i].index(min(triangle[i][-1], triangle[i][-2])))
        else:
            dp[i].append(min(triangle[i][dp[i - 1][1] - 1], triangle[i][dp[i - 1][1]], triangle[i][dp[i - 1][1] + 1]))
            dp[i].append(triangle[i].index(min(triangle[i][dp[i - 1][1] - 1], triangle[i][dp[i - 1][1]], triangle[i][dp[i - 1][1] + 1])))
    # return dp
    return sum([dp[i][0] for i in range(len(dp))])


def minimumTotal_alt(triangle):  # O(mn) both 
    """
    make dp of the squared size
    First and last columns are filled out separately 
    """
    m = len(triangle)
    dp = [[0 for i in range(m)] for _ in range(m)]
    dp[0][0] = triangle[0][0]
    for i in range(1, m):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            else:
                if i == j:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    return min(dp[-1])


def minimumTotal_traverse(triangle):
    if not triangle:
        return 0
    rows = len(triangle)
    if rows == 1:
        return triangle[0][0]
    
    # Traverse from the second last row to the first row.
    for i in range(rows - 2, -1, -1):
        # Then iterate through every element in this row.
        # Every element in this row = (current value) + min(left, right)
        for j in range(i + 1):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
    # At the end, the value of first row is the answer.
    return triangle[0][0]


def minimumTotal_another(triangle):  # DOESN'T WORK FOR EDGE CASES
    dp = [[0] * len(triangle[-1]) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for row in range(1, len(triangle)):
        for col in range(row):
            if col == 0:
                # dp[row][col] = dp[row - 1][col] + min(triangle[row][col], triangle[row][col + 1])
                dp[row][col] = dp[row - 1][col] + triangle[row][col]
            elif col == len(triangle[row]) - 1:
                # dp[row][col] = dp[row - 1][col] + min(triangle[row][col - 1], triangle[row][col])
                dp[row][col] = dp[row - 1][col - 1] + triangle[row][col]
            else:
                dp[row][col] = triangle[row][col] + min(dp[row - 1][col - 1], triangle[row][col])
                # dp[row][col] = dp[row - 1][col] + min(triangle[row - 1][col - 1], triangle[row - 1][col + 1])
    print(dp)
    return min(dp[-1])
        

if __name__ == '__main__':
    # print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    # print(minimumTotal([[-10]]))
    # print(minimumTotal([[-1], [2, 3], [1, -1, -3]]))
    # print(minimumTotal_alt([[-1], [2, 3], [1, -1, -3]])) # this case should return 0, as it does above
    # print(minimumTotal_traverse([[-1], [2, 3], [1, -1, -3]]))
    # print(minimumTotal_traverse([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
