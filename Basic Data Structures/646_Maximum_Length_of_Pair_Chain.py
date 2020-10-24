def findLongestChain(pairs):
    """"
    Sort by first element
    Then it becomes longest increasing subsequence 
    """
    if len(pairs) <= 1: return len(pairs)
    pairs.sort(key = lambda x: x[0])
    dp = [1] * len(pairs)
    for r in range(len(pairs)):
        for l in range(r):
            if pairs[r][0] > pairs[l][1]:
                dp[r] = max(dp[r], dp[l] + 1)
    return max(dp)


if __name__ == '__main__':
    print(findLongestChain([[1, 2], [2, 3], [3, 4]]))