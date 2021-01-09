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


def longestPalindromeSubseq_alt(s):  # O(n^2) and O(n)
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
                cur[j] = max(pre[j], cur[j - 1])
        pre = cur        
    return pre[-1]   


def longestPalindromeSubseq_bottoms_up(s):  # O(n^2) and O(n^2)
    """
    Diagonals filled with 1 (b/c strings of one character are palindromes)
    Then start two loops: the starting index is the second last character
    Ending index is the starting + 1 index
    If letters at indices aren't the same, choose the max between the element to the left and below
    If the same, add 2 to the value in the left lower corner
    We fill out the triangle above the main diagonal.
    The answer is in the right upper corner 
    """
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):  # main diagonal
        dp[i][i] = 1 
    for st in range(len(s) - 2, -1, -1):
        for en in range(st + 1, len(s)):
            if s[st] != s[en]:
                dp[st][en] = max(dp[st + 1][en], dp[st][en - 1])  # it chooses the max between either skipping the left or the right element 
            else:
                dp[st][en] = 2 + dp[st + 1][en - 1]
    return dp[0][-1]


if __name__ == '__main__':
    # print(longestPalindromeSubseq('abdbca'))m
    # print(longestPalindromeSubseq_alt('abdbca'))
    print(longestPalindromeSubseq_bottoms_up('abdbca'))
    print(longestPalindromeSubseq_bottoms_up('bbbab'))
    print(longestPalindromeSubseq_bottoms_up('cbbd'))