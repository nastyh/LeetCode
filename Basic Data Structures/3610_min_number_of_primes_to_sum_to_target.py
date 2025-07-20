class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        """
        O(mn), m -- number of primes, n -- target sum
        O(m+n), dp array of size n + 1, primes list of size m

        First func generates the first m prime numbers and stores as a list 
        It's the incremental implementation
        For each candidate n, test whether it's divisible by any previous prime less than or equal to
        sqrt(n). Because if n is divisible by anything larger than sqrt(n), it has to be divisble by
        something smaller, too. So it's redundant to go and check anything beyond sqrt(n)

        Then we do it like a coin change problem 
        dp list 
        consider each prime number that we generated, it's p
        look at every value i from p to n (result)
        if we can form i - p with some number of primes dp[i-p], 
        then we can form i by adding p one more time --> dp[i-p] + 1
        Check whether the current dp[i] is better (smaller) 
        or dp[i-p] + 1 is better (reuse the prev prime p one more time)
        """
        def _first_m_primes(m):
            if m <= 0:
                return []
            primes = [2]
            n = 3
            while len(primes) < m:
                root = n ** 0.5
                for p in primes:
                    if p > root:
                        primes.append(n)
                        break
                    if n % p == 0:
                        break
                n += 2            # skip even numbers
            return primes[:m]

        primes = _first_m_primes(m)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 can be formed with 0 primes
        for prime in primes:
            for i in range(prime, n + 1):
                dp[i] = min(dp[i], dp[i - prime] + 1)

        return dp[n] if dp[n] != float('inf') else -1
