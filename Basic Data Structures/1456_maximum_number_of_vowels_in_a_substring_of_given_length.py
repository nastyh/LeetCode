class Solution:
    def maxVowels(self, s: str, k: int) -> int:  # times out
        # create a window of size k and move it to the end of the string
        # see how many vowels in each window, update the global result 
        vowels = 'aeiou'
        if len(s) == 0: return
        if k > len(s): return
        l, curr, curr_l, glob_l = 0, '', 0, -math.inf
        while l + k - 1 < len(s): # moving the window 
            curr = s[l:l + k]
            curr_l = sum([1 for el in curr if el in vowels])
            glob_l = max(glob_l, curr_l)
            l += 1
        return glob_l

    def maxVowels_alt(self, s: str, k: int) -> int: # O(1) both 
        #starts creating a window. While creating, increment the number of vowels.
        # Once its length is more than k, start moving the left border of the window to the right.
        # If you remove a vowel, decrement the respective counter. Once you've built a string of a 
        # required length, update the glob_l result.
        vowels = 'aeiou'
        if len(s) == 0: return
        if k > len(s): return
        l_ix, r_ix, length, glob_length = 0, 0, 0, -math.inf 
        for r_ix in range(len(s)):
            r_el = s[r_ix]
            if r_el in vowels:
                length += 1
            while r_ix - l_ix + 1 > k:
                l_el = s[l_ix]
                if l_el in vowels:
                    length -= 1
                l_ix += 1
            if r_ix - l_ix + 1 == k:
                glob_length = max(glob_length, length)
        return glob_length

    def maxVowels_more(self, s: str, k: int) -> int: 
        vowels = 'aeiou'
        # edge cases
        if len(s) == 0: return
        if k > len(s): return
        l, r = 0, k
        curr_res, glob_res = 0, -math.inf
        # find out the result for the first window: starts from zero goes to the k-th element
        # it's a one-time operation
        # now just move the window of the fixed size
        # till the right part hits the end of the string
        for ix in range(l, r):
            if s[ix] in vowels:
                curr_res += 1
                glob_res = max(glob_res, curr_res)
        while r < len(s):
            if s[l] in vowels:
                curr_res -= 1 # don't have it anymore
            if s[r] in vowels:
                curr_res += 1
            glob_res = max(glob_res, curr_res)
            l += 1
            r += 1
        return glob_res
    
