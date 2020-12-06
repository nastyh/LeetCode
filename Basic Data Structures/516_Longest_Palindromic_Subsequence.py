def longestPalindromeSubseq(s):  # O(n^2) and O(n^2)
    dp =[[0] * len(s) for _ in range(len(s))] 
    for i in reversed(range(len(s))):
        for j in range(i, len(s)):
            if i == j:
                dp[i][j] = 1
                continue
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:    
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][len(s) - 1]


def longestPalindromeSubseq_alt(s):  # O(n^2) and O(1)
    pre = [0] * len(s)  
	for i in reversed(range(len(s))):
		cur = [0] * len(s)  
		for j in range(i, len(s)):
			if i == j:
				cur[j] = 1
				continue
			if s[i] == s[j]:
				cur[j] = pre[j-1] + 2
			else:    
				cur[j] = max(pre[j], cur[j-1])
		pre = cur        
	return pre[-1]   