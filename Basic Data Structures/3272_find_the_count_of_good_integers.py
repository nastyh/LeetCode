from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        # skip = n & 1 # shorthand (using bitwise and) for checking if n is odd.
        if n % 2 == 1: 
            skip = 1
        else: 
            skip = 0
        # if n is odd, skip is 1, otherwise, skip is 0
        # Enumerate the number of palindrome numbers of n digits
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            # If the current palindrome number is a k-palindromic integer
            if palindromicInteger % k == 0:
                sorted_s = "".join(sorted(s))
                dictionary.add(sorted_s)

        fac = [factorial(i) for i in range(n + 1)]
        # a list of factorials from 0! up to n! which is used in counting
        # the permutations of the n digits later 
        ans = 0
        for s in dictionary:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            # Calculate permutations and combinations
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                tot //= fac[x]
            ans += tot

        return ans