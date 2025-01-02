class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """
        O(M+N), pref O(M), all queries O(n)
        O(M) for pref
        create a prefix sum array prefixSum to store the cumulative counts
        of vowel strings in words. prefixSum[i] would contain the total number
        of vowel strings from the first element of the array up to index i
        (the prefix array words[0:i]). Populating this prefixSum array would only take one linear scan ac
        """
        vowels_d = {"a", "e", "i", "o", "u"}
        res = [0] * len(queries)
        pref = [0] * len(words)
        sums = 0
        for i in range(len(words)):
            curr = words[i]
            if (curr[0] in vowels_d and curr[-1] in vowels_d):
                sums += 1
            pref[i] = sums
        for i in range(len(queries)):
            curr_q = queries[i]
            res[i] = pref[curr_q[1]] - (
                0 if curr_q[0] == 0 else pref[curr_q[0] - 1]
            )
        return res