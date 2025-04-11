class Solution:
    def countSymmetricIntegers_symmetric(self, low: int, high: int) -> int:
        """
        O(high - low)
        O(1) nothing to store
        If it is a two-digit number and is a multiple of 11, then it is a symmetric integer
        If it is a four-digit number, calculate the sum of the thousands and hundreds digits,
        as well as the sum of the tens and ones digits. If they are equal, it is a symmetric (even) integer.
        """
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            if 1000 <= a < 10000:
                left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                if left == right:
                    res += 1
        return res
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        O(high - low) to go over the range
        O(high - low) to save a portion with the even number of digits
        Do what they ask
        _helper creates a list of integers (as strings) between low and high
        that are of the even length
        go thru the list, cut in two halves using middle_ix
        calculate the sums, compare, increment res and return 
        """
        res = 0
        def _helper(l, h):
            res = []
            for num in range(l, h+1):
                if len(str(num)) % 2 == 0:
                    res.append(str(num))
            return res 
        all_candidates = _helper(low, high)
        for num in all_candidates:
            middle_ix = len(num) // 2
            left_side = num[:middle_ix]
            right_side = num[middle_ix:]
            left_sum = sum(int(n) for n in left_side)
            right_sum = sum(int(n) for n in right_side)
            if left_sum == right_sum:
                res += 1
        return res
