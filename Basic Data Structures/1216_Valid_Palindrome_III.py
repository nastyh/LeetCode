def isValidPalindrome(s, k):  # O(n^2) both 
    ## RC ##
    ## APPROACH : DP ##
    ## LOGIC ##
    ## 1. Draw Bottom Up DP Table
    ##      a) when length == 1, no change required, so dp[i][j] = 0
    ##      b) when length == 2, if string is aa or bb, we do not require any k, so take previous substring value i.e from diagonal. else we take as 1. i.e we require 1 char to change
    ##      c) when length > 2, we can generalize it as, if s[i] == s[j] then we can remove ith character which requires one operation and take previous s[i+1][j] value or 1 + dp[i][j-1] or we remove both chars take previous substring i.e 2 + dp[i+1][j-1]
    
    ##  STACK TRACE ##
    ## EXAMPLE : BACABAAA ##
    # [
    #     [0, 1, 2, 1, 0, 1, 2, 3], 
    #     [0, 0, 1, 0, 1, 2, 1, 2], 
    #     [0, 0, 0, 1, 2, 1, 2, 2], 
    #     [0, 0, 0, 0, 1, 0, 1, 1], 
    #     [0, 0, 0, 0, 0, 1, 1, 1], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 0]
    # ]
    dp = [ [0 for _ in s ] for _ in s]
    
    for i in range(len(dp) - 2, -1, -1):  # second last
        for j in range(i + 1,len(dp)): # right from second last
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(1 + dp[i][j - 1], 1 + dp[i + 1][j], 2 + dp[i + 1][j - 1])
    return dp[0][-1] <= k

    
def isValidPalindrome_space_efficient(s, k): # O(n^2) and O(n)
    """
    Doesn't pass "abbababa" 1 
    """
    dp = [0] * len(s)
    temp, prev = 0, 0
    for i in range(len(s) - 2, -1, -1):
        prev = 0
        for j in range(i + 1, len(s)):
            temp = dp[j]
            if s[i] == s[j]:
                dp[j] = prev
                dp[j] = 1 + min(dp[j], dp[j - 1])
            prev = temp
    return dp[-1] <= k