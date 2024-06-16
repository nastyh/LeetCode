class Solution:
    def strStr_mine(self, haystack: str, needle: str) -> int:
        """
        h_ix is the left index for haystack
        curr_ix expands from h_ix to the length of needle
        so we have a window of the size needs at the end
        we restart curr_ix to zero b/c it's relative to h_ix, and it is used for going over
        needle again from scratch once we restart the process
        """
        h_ix, curr_ix = 0, 0
        while h_ix < len(haystack):
            if haystack[h_ix] == needle[curr_ix]:
                # if the latter match, keep looking by extending the right side
                curr_ix += 1 # move through needle
                # we are of the size of needle
                if curr_ix == len(needle):
                    return h_ix - curr_ix + 1
            else:
                h_ix -= curr_ix # curr ix is never larger than needle 
                curr_ix = 0
            h_ix += 1 # move through heystack
        return -1
        
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

    def strStr_another_pythonic(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
