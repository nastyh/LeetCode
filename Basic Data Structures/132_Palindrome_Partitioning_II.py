def minCut(self, s):
    length = len(s)
    palindromes = [[False] * length for _ in range(length)]

    #computed values for substring of length 1
    for i in range(length):
        palindromes[i][i] = True

    #Now filling up the palindrome table for substring Length greater than 1!
    for substringLength in range(2,length+1):
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