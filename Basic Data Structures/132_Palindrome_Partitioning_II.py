def minCut(s):
    length = len(s)
    palindromes = [[False] * length for _ in range(length)]

    #computed values for substring of length 1
    for i in range(length):
        palindromes[i][i] = True

    #Now filling up the palindrome table for substring Length greater than 1!
    for substringLength in range(2,length + 1):
        #We iterate through every substring of substringLength
        for i in range(0,length  -substringLength + 1):
            j = i + substringLength - 1
            #Calculation Logic:
            #For substring of SubstringLength we check if first and last character matches and in-between string is palindrome or not
            if substringLength == 2:
                palindromes[i][j] = s[i] == s[j]
            else:
                palindromes[i][j] = s[i] == s[j] and palindromes[i + 1][j - 1]

    minCutRequired = [float('inf')]*length

    for i in range(0,length):
        if palindromes[0][i]:
            minCutRequired[i] = 0
        else:
            minCutRequired[i] = minCutRequired[i - 1] + 1
        #optimising the cuts required by checking if there is any palindrome in-between!
        for j in range(1, i):
            if palindromes[j][i] and minCutRequired[j - 1] + 1 < minCutRequired[i]:
                minCutRequired[i] = minCutRequired[j - 1]+1
    return minCutRequired[-1]


def minCut_alt(s):  # O(n^2) and O(n^2)
    if not s : return 0
    dp = [[True] * len(s) for i in range(len(s))]        # DP Matrix of booleans -> dp[i][j] - TRUE if 's[i: j + 1]' is palindrome, else FALSE
    cuts = [float("inf")] * len(s)                       # DP cuts array -> indicates min cuts require till ith entry
    # We first find all palindromic substrings
    for r in range(1, len(s)):
        for c in range(len(s) - r):
            if not (s[c] == s[c + r] and dp[c + 1][c + r - 1]):
                dp[c][c + r] = False
    # For ith column, we check every entry till diagonal element
    # If dp[j][i] is true, implies 's[j: i + 1]'' is palindrome and
    # we check if we get minimum cuts considering this substring or not  
    for i in range(len(s)):
        for j in range(i + 1):
            if dp[j][i]:
                cuts[i] = min(cuts[i], (cuts[j - 1] + 1) if j - 1 >= 0 else 0)     
    return cuts[-1]