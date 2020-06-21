def wordBreak(s, wordDict):
    """
    The DP part of the problem can be like this: the substring up to but not including index i satisfies the question. To solve this, we can further divide
    the substring (up to i) into two parts, s[0:j] and s[j:i]. dp[j] provides the answer for s[0:j] and we only need to verify s[j:i] is in wordDict or not.
    If there exists a j that satisfies both requirements, then dp[i] is True.
    """

    wordDict = set(wordDict)
    # a substring [0:i] satisfies the requirement
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j: i] in wordDict:
                dp[i] = True
                break

    return dp[-1]

if __name__ == '__main__':
    print(wordBreak("leetcode",["leet", "code"]))
    print(wordBreak("applepenapple",["apple", "pen"]))
    print(wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"]))