from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        """
        O(logn(finish)*10)
        enumerate the numbers we can fill in for each digit, the length of the number of digits is
        log(finish), there are 10 digits ([0; 9])
        O(log(finish)) -- array of the same length as a the number of digits to memoize the result 
        of each digit

        preprocess:
        convert to strings so we can go digit by digit 
        zfill(n) to pad the low string with leading zeroes so it's of the same length as high
        important, since for the DP purposes we compare digit by digit precisely

        the first pre_len digits can vary 
        the remaining digits (positions from pre_len to n - 1) are forced to match those from s

        """
        low = str(start)
        high = str(finish)
        n = len(high)
        low = low.zfill(n)  # align digits
        pre_len = n - len(s)  # prefix length. the number of digits in our number that are not part of the fixed suffix s

        @cache
        def dfs(i, limit_low, limit_high):
            """
            i -- current digit index
            limit_low -- boolean indicating whether the digits chosen so far are still at the lower bound
            If True, the curr digit must be at leazt low[i]. False, the lower bound doesn't apply 
            limit_high -- same but for the higher bound. True -- current digit cannot exceed high[i]
            False, upper bound isn't longer active 
            """
            # recursive boundary
            if i == n:  # base case 
                return 1
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            res = 0
            if i < pre_len:
                for digit in range(lo, min(hi, limit) + 1):
                    res += dfs(
                        i + 1,
                        limit_low and digit == lo,
                        limit_high and digit == hi,
                    )
            else:
                x = int(s[i - pre_len])
                if lo <= x <= min(hi, limit):
                    res = dfs(
                        i + 1, limit_low and x == lo, limit_high and x == hi
                    )

            return res

        return dfs(0, True, True) # starts at the first digit, initially, the num is at the lower and upper boundaries 