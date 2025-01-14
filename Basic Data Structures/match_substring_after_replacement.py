"""
Given two strings, s, and sub, along with a 2D character array mappings, we want to determine if it is possible to make
the sub a substring of s by replacing characters according to the provided mappings. Each mapping consists of a pair [oldi, newi],
indicating that we can replace the character oldi in sub with newi.
The replacement can be performed any number of times, but each character in sub can be replaced at most once.
We need to return true if it is possible to create sub as a substring of s using the given replacements, and false otherwise.
"""
from collections import defaultdict
def can_form_substring(s: str, sub: str, mappings: list[list[str]]) -> bool:
    """
    O(nm), n length of s, m len of sub
    O(k), size of the dict
    dictionary stores store all possible replacements for each character in sub
    we check each substring of s (of length equal to sub) dynamically against sub using the mapping dictionary.
    """
    # Step 1: Create a mapping dictionary
    mapping_dict = defaultdict(set)
    for old, new in mappings:
        mapping_dict[old].add(new)
    for char in sub:
        mapping_dict[char].add(char)  # Include the original character itself
    # Step 2: Helper function to check if a window in `s` matches `sub` with replacements
    def matches_with_mappings(window: str, sub: str) -> bool:
        for i, char in enumerate(sub):
            if window[i] not in mapping_dict[char]:
                return False
        return True

    # Step 3: Sliding window to check all substrings of length len(sub) in `s`
    sub_len = len(sub)
    for i in range(len(s) - sub_len + 1):
        if matches_with_mappings(s[i:i + sub_len], sub):
            return True

    return False

def matchReplacement_another(self, s, sub, mappings):
        def compute_lps(self, s, m):
            lps = [0] * len(s)
            j = 0
            for i in range(1, len(s)):
                while j > 0 and (s[i] != s[j] and (s[i] not in m or s[j] not in m[s[i]])):
                    j = lps[j - 1]
                j += int(s[i] == s[j] or (s[i] in m and s[j] in m[s[i]]))
                lps[i] = j
            return lps

        m = {}
        for p in mappings:
            if p[0] not in m:
                m[p[0]] = set()
            m[p[0]].add(p[1])

        lps = self.compute_lps(sub, m)
        i, j = 0, 0
        while i < len(s):
            if s[i] == sub[j] or (sub[j] in m and s[i] in m[sub[j]]):
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
            if j == len(sub):
                return True
        return False
