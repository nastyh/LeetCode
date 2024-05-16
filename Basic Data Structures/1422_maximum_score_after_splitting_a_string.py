class Solution:
    def maxScore(self, s: str) -> int:
        # need to cut a string in a way so that 
        # the left part has the max number of zeroes
        # and the right part has the max number of ones
        zeroes = 0
        ones = s.count('1')
        res = 0
        for i in range(len(s) - 1):  # don't want to add the last element 
            if s[i] == '0':
                zeroes += 1
            else:
                ones -= 1 # we found a one in the left portion
            res = max(res, zeroes + ones)
        return res