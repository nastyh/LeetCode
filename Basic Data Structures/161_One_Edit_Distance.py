def isOneEditDistance_optimal(s, t):  # O(n) both b/c strings are immutable
    """
    All work is done in the _helper() func. It takes two strings as params. The first has to be not longer than the second
    First, cover the edge case
    Second, start comparing element by element initializing a loop using the shorter string as a base:
    if elements at respective positions are not the same, it still can be True if everything else after is the same
    Everything means that there is the same number of characters in both strings and characters are the same to the right from different elements
    If lengths of strings are different, everyting should be the same 
    If the number of characters to the right is not the same, this additional character should be the only difference
    Third, check the lengths and be done
    """
    def _helper(str1, str2):  # first is always <= second
        if len(str2) - len(str1) > 1:
            return False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if len(str1) == len(str2):
                    return str1[i + 1:] == str2[i + 1:]
                else:
                    return str1[i:] == str2[i + 1:]
        return len(str1) + 1 == len(str2)
    
    if len(s) > len(t):
        return _helper(t, s)
    else:
        return _helper(s, t)


def isOneEditDistance_brute_force_dp(s, t):  # TLE O(nm) both 
    """
    Based on the approach developed in 072 Edit Distance (Levenstein distance)

    dp is a matrix of word1 + 1 and word2 + 1 sizes
    first row means that len(word1) is equal to zero. To make word2 equal to zero, we need to remove as many elements as in len(word2). Thus, we can fill out the first row
    The same logic applies to the first col. But here we're trying to make word1 equal to zero
    When we move along the rows/cols, it means that we're considering longer strings
    Then start filling out from the cell (1, 1)
    Insert operation: res(m, n) = res(m, n - 1) + 1. Moving horizontally
    Remove operation: res(m, n) = res(m - 1, n) + 1. Moving vertically
    Replace operation: res(m, n) = res(m - 1, n - 1) + 1. Moving diagonally
    Always choose the min of the three and fill out the table. 
    If the last cell is one, it means strings are one edit away from each other 
    """
    if abs(len(s) - len(t)) > 1: return False
    dp = [[None] * (len(s) + 1) for _ in range(len(t) + 1)]
    for col in range(len(s) + 1):
        dp[0][col] = col
    for row in range(len(t) + 1):
        dp[row][0] = row 
    for row in range(1, len(t) + 1):
        for col in range(1, len(s) + 1):
            if t[row - 1] == s[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                _insert = dp[row][col - 1]
                _remove = dp[row - 1][col]
                _replace = dp[row - 1][col - 1]
                dp[row][col] = 1 + min(_insert, _remove, _replace)
    return dp[-1][-1] == 1


def isOneEditDistance_optimized_dp(s, t):  # TLE O(nm) and O(2m) where m is the length of string t
    dp = [[0 for i in range(len(t) + 1)] for j in range(2)]
    for i in range(len(t) + 1):
        dp[0][i] = i
    for i in range(1, len(s) + 1):
        dp[i % 2][0] = i;
        for j in range(1, len(t) + 1):
            cost = 1 if s[i - 1] != t[j - 1] else 0;
            dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1] + cost, dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1)
    return dp[len(s) % 2][len(t)] == 1


if __name__ == '__main__':
    print(isOneEditDistance_brute_force_dp('ab', 'acb'))
    print(isOneEditDistance_brute_force_dp('', ''))
    print(isOneEditDistance_brute_force_dp('a', ''))
    print(isOneEditDistance_brute_force_dp('', 'A'))
    print(isOneEditDistance_optimized_dp('ab', 'acb'))
    print(isOneEditDistance_optimized_dp('', ''))
    print(isOneEditDistance_optimized_dp('a', ''))
    print(isOneEditDistance_optimized_dp('', 'A'))