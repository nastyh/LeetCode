class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        O(len(str1)*len(str2)) to process both to fill out the dp table
        Same for space, since dp
        first compute the longest common subsequnce (LCS)
        Use it to merge the strings together into the shortest subsequence.
        LCS is the common backbone shared by both strings. Then we insert the characters around 
        the backbone to obtain the shortest sequence
        """
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]  # one extra row and col
        res = []
        """
        fill from (1, 1)
        if the characters match, take the value from the cell up-left + 1
        if they don't, take max of the values from the cell to the left and the cell above 
        """
        for i in range(1, len(str1) + 1):  # i means cols
            for j in range(1, len(str2) + 1):  # j means rows
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # Reconstruct the LCS
        lcs = []
        i, j = len(str1), len(str2)
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                lcs.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1
        lcs.reverse()
        # merge str1 and str2 using the LCS
        # This step ensures that all characters from both strings appear in the final result,
        # and the order is preserved to ensure that both strings are subsequences.
        i, j = 0, 0
        for c in lcs:
            while i < len(str1) and str1[i] != c:
                # Append non-LCS characters from str1.
                res.append(str1[i])
                i += 1
            # Append non-LCS characters from str2.
            while j < len(str2) and str2[j] != c:
                res.append(str2[j])
                j += 1
            # Append the LCS character and move both pointers.
            res.append(c)
            i += 1
            j += 1
        # Append any remaining characters after processing the LCS.
        res.extend(str1[i:])
        res.extend(str2[j:])
        return ''.join(res)