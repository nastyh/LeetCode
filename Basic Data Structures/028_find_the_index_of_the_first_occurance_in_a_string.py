class Solution:
    def strStr(self, haystack: str, needle: str) -> int: # O((N - M + 1) * M) and O(1)
        """
        two pointers
        go thru haystack with a loop that is from 0
        to len(haystack) - len(needle) + 1
        inside compare characters of the needle string with the chars
        in the haystack string starting from the current index. It's done
        using j
        If match, increment j and keep going
        If j gets to the length of the needle string, there is a match.
        Return i 

        """
        l, r = 0, 0
        while l < len(haystack):
            if haystack[l] == needle[r]:
                r += 1
                if r == len(needle):
                    return l - r + 1
            else:
                l -= r  # Move back l to the beginning of the current match attempt
                r = 0  # Reset r
            l += 1 # keep moving the loop
        return -1
        