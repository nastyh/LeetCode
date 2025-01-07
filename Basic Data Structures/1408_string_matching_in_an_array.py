class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        brute force
        O(n^2*k), n num of words, k the ave length of words
        O(n) for res

        Iterate through each word: Use two nested loops to compare each word with every other word in the list.
        For a given pair of words, check if one word is a substring of the other.
        Ensure the indices of the words are not the same to prevent self-comparison.
        If a word is found to be a substring of another, add it to the result list and break out of the inner loop to avoid duplicates.
        """
        res = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    res.append(word)
                    break
        return res
    
    def stringMatching_kmp(self, words: List[str]) -> List[str]:
        """
        O(n^2*k)
        O(k)
        Compute the LPS (Longest Prefix Suffix) array for the pattern (s) to optimize matching.
        Use the LPS array to efficiently match the pattern (s) in the text (t).
        Return True if s is found as a substring in t, otherwise False.
        Iterate over each word in the array.
        Use the is_substring function to check if a word is a substring of any other word.

        """
        def is_substring(s, t):
        # KMP algorithm to check if s is a substring of t
            m, n = len(s), len(t)
            lps = [0] * m
            j = 0  # index for s
            
            # Compute LPS (longest prefix suffix) array for the pattern s
            for i in range(1, m):
                while j > 0 and s[j] != s[i]:
                    j = lps[j - 1]
                if s[j] == s[i]:
                    j += 1
                lps[i] = j
            
            # Use LPS array to search for s in t
            j = 0  # index for s
            for i in range(n):  # index for t
                while j > 0 and s[j] != t[i]:
                    j = lps[j - 1]
                if s[j] == t[i]:
                    j += 1
                if j == m:
                    return True  # Found substring
            return False

        result = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and is_substring(word, other):
                    result.append(word)
                    break
        return result
