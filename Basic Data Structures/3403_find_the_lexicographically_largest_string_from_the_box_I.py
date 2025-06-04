class Solution:
    def answerString_two_pointers(self, word: str, numFriends: int) -> str:
        """
        O(n) and O(1)
        Helper finds the lexicographically last substring of the string s.
        It returns the suffix of s that is lexicographically largest among all suffixes.

        Truncate it to max_len = n - numFriends + 1, which is the maximum size allowed for any part in the split.
        Return the prefix of last of that length
        """
        def _lastSubstring(s: str) -> str:
            """
            i: current best candidate start index for the last substring
            j: the next candidate start index to compare
            k: offset to compare characters from i and j
            """
            i, j, n = 0, 1, len(s)
            while j < n:
                """
                Compare suffix starting at i vs. suffix at j.
                Keep advancing k while characters match.
                """
                k = 0
                while j + k < n and s[i + k] == s[j + k]:
                    """
                    If at the first differing position s[i + k] < s[j + k], the suffix starting at j is better.
                    Update i = j to mark the new candidate, and advance j.
                    """
                    k += 1
                if j + k < n and s[i + k] < s[j + k]:
                    i, j = j, max(j + 1, i + k + 1)
                else:
                    """
                    If s[i + k] >= s[j + k], discard j and move to next position after match.
                    """
                    j = j + k + 1
            return s[i:]
        if numFriends == 1:
            return word
        last = _lastSubstring(word)
        n, m = len(word), len(last)
        return last[: min(m, n - numFriends + 1)]


    def answerString_sort_suffix(self, word: str, numFriends: int) -> str:
        """
        O(nlogn) due to sorting
        O(n^2) in space in the worst case to store all suffix strings
        """
        n = len(word)
        if numFriends == 1:
            return word

        max_len = n - (numFriends - 1)

        # Build list of suffixes with their starting indices
        suffixes = [(word[i:], i) for i in range(n)]
        # Sort suffixes in reverse lexicographic order
        suffixes.sort(reverse=True)

        # Get the first valid prefix up to max_len
        for suff, i in suffixes:
            candidate = suff[:max_len]
            return candidate  # First is the largest due to sorting


    def answerString_linear(self, word: str, numFriends: int) -> str:
        """
        TIMES OUT 
        """
        n = len(word)
        max_len = n - (numFriends - 1)  # Max possible length for any part in a valid split
        best = ""

        if numFriends == 1:
            return word

        for i in range(n):
            # Only consider substrings that can fit within the max_len limit
            for l in range(1, min(max_len, n - i) + 1):
                substr = word[i:i + l]
                if substr > best:
                    best = substr

        return best
    def answerString_dfs(self, word: str, numFriends: int) -> str:
        """
        TIMES OUT
        """
        n, res = len(word), ""
        def _dfs(start, splits, path):
            nonlocal res
            if splits == numFriends - 1:
                if start < n:
                    path.append(word[start:])  # add the last remaining part
                    for part in path:
                        if part > res:
                            res = part
                    path.pop()
                return
            for end in range(start + 1, n - (numFriends - splits - 1) + 1):
                path.append(word[start:end])
                _dfs(end, splits + 1, path)
                path.pop()

        _dfs(0, 0, [])
        return res
