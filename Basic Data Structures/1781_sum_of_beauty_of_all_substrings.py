import math


class Solution:
    def beautySum_dp(self, s: str) -> int:
        """
        O(n^2*26)
        O(n)
        kinda worse than the brute force below
        create a 2D list prefix of size (n+1)×26.
        For each index i in the string, we copy the counts from prefix[i] into prefix[i+1] and update the count for the current character.
        For every substring defined by indices i and j, we compute the frequency of each character
        determine the maximum and minimum (nonzero) frequencies for that substring and add their difference to res
        """
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]
        res = 0
        for i in range(n):
            for c in range(26):
                prefix[i + 1][c] = prefix[i][c]
            prefix[i + 1][ord(s[i]) - ord('a')] += 1

        for i in range(n):
            for j in range(i, n):
                max_f = 0
                min_f = math.inf
                # For each character, calculate its frequency in the substring.
                for c in range(26):
                    freq = prefix[j + 1][c] - prefix[i][c]
                    if freq > 0:
                        max_f = max(max_f, freq)
                        min_f = min(min_f, freq)
                if min_f != math.inf:
                    res += max_f - min_f

        return res
        
    def beautySum(self, s: str) -> int:
        """
        O(n^2) b/c of two loops and all the substrings
        O(1) since the dicts never become bigger than 26 elements
        two loops:
        for each element look to the right,
        create a substring, put the frequencies
        into a brand new dict
        take max and min values for each dict,
        contribute to res 
        """
        res, n = 0, len(s)
        for i in range(n):
            d = {}
            for j in range(i, n):
                if s[j] not in d:
                    d[s[j]] = 1
                else:
                    d[s[j]] += 1

                max_f = max(d.values())
                min_f = min(f for f in d.values() if f > 0)
                res += max_f - min_f
        return res