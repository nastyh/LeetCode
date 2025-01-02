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

    def maxScore_another(self, s: str) -> int:
        """
        O(n) and O(1)
        between a split at index i and index i + 1,
        we are only changing one character (more specifically, moving it from the right substring to the left substring),
        leaving the other characters unchanged. Instead of iterating over the entire string for each split,
        we only need to check the moved character and calculate the score for the new split based on the previous split.
        """
        zeroes_count, ones_count = 0, 0
        res = 0
        for ch in s:
            if int(ch) == 1:
                ones_count += 1
        for candidate in s[:-1]:
            if candidate == '0':
                zeroes_count += 1
            else: 
                ones_count -= 1
            res = max(res, zeroes_count + ones_count)
        return res

    def maxScore_one_pass(self, s: str) -> int:
        ones, zeroes, res = 0 , 0 , -math.inf
        for candidate in s[:-1]:
            if candidate == '1':
                ones += 1
            else:
                zeroes += 1
            res = max(res, zeroes - ones)
        if s[-1] == '1':
            ones += 1
        return ones + res
