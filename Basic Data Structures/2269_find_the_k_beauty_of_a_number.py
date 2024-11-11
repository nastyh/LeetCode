class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        """
        O(n) both
        l and r allows to get a candidate of a size k
        int(candidate) != 0 takes care of "00"-like cases
        then just build the answer and move to the right 
        """
        num_s = str(num)
        res = 0
        l = 0
        r = l + k
        while r <= len(num_s):
            candidate = num_s[l:r]
            if int(candidate) != 0 and num % int(candidate) == 0:
                res += 1
            l += 1
            r += 1
        return res