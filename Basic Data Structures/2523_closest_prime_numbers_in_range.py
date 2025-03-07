import math
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """
        O(Rlog(log(R)) + R - L)
        O(Rlog(log(R))) where R is the upper limit is for the helper
        Then iterate from left to right, so minus left
        O(R) for the list of prime numbers 

        Helper func uses the Sieve of Eratosthenes alg
        to find the primes that are <= given num 
        does so by iteratively marking as composite (i.e., not prime)
        the multiples of each prime, starting with the first prime number, 2. 
        The multiples of a given prime are generated as a sequence of numbers starting from that prime
        """
        def _helper(num):
            # returns a list of bools from 1 to n where True means a prime number
            res = [True for i in range(num+1)]
            p = 2
            while p*p <= num:
                if res[p] == True: # means a prime number
                    for i in range(p*p, num + 1, p): # all multiples of it become False
                        res[i] = False
                p += 1
            return res
        bools = _helper(right)
        # turn it into a list of prime numbers instead of booleans 
        all_primes = [i for i in range(2, len(bools)) if bools[i]]
        # cut it from the left side
        our_primes = [n for n in all_primes if n >= left]
        # then just compare the numbers next to each other 
        curr_diff, smallest_diff, ans = 0, math.inf, [-1, -1]
        # edge case when the input is like [4;6], thus, there is only one
        # prime number [5], and we return [-1;-1] per question 
        if len(our_primes) < 2:
            return ans
        # compare numbers next to each other
        for ix in range(len(our_primes) - 1):
            curr_diff = our_primes[ix+1] - our_primes[ix]
            if curr_diff < smallest_diff:
                # if we find a better match, update the ans 
                smallest_diff = curr_diff
                ans[0], ans[1] = our_primes[ix], our_primes[ix+1]
        return ans
        