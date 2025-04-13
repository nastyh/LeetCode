from itertools import product


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        O(logn)
        pow() internally implements exponentiation by squaring
        So O(log(even_count)) + O(log(odd_count)) --> O(logn)
        O(1) nothing to store

        Even indices (0, 2, 4...)
        These digits should be even. There are five: 0, 2, 4, 6, 8
        Odd indices (1, 3, 5...)
        These digits should be any of the primes from the question: 2, 3, 5, 7 (four)
        the answer is 
        5^(number of even positions) + 4^(num of odd positions)
        calculate the number of even and odd positions
        use the formula, divide by mod per question 
        """
        mod, even_count, odd_count = 10**9 + 7, (n + 1) // 2, n // 2
        res = (pow(5, even_count, mod) * pow(4, odd_count, mod)) % mod
        return res 
    
    def countGoodNumbers_brute_force(self, n: int) -> int:
        """
        Times out by it's do what they tell
        """
        res, candidates = 0, []
        def _helper(s):
            # Check even-indexed positions: must be even
            for i in range(0, len(s), 2):
                if int(s[i]) % 2 != 0:
                    return False
            # check odds 
            for i in range(1, len(s), 2):
                if s[i] not in {'2', '3', '5', '7'}:
                    return False
            return True 
        for digits in product("0123456789", repeat=n):
            s = "".join(digits)
            if _helper(s):
                res += 1
                candidates.append(s)
        return res 