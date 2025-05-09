from collections import defaultdict


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        """
        O(N^2) both
        A permutation is balanced when the sum of the digits placed
        at even indices (0-based) equals the sum of the digits placed at odd indices.
        If the total digit-sum is odd, S = 2 * sum_even is impossible ⇒ answer = 0.
        Choose how many copies of each digit go to the even slots
        """
        MOD = 10**9 + 7
        velunexorai = num # keeps the original input string midway through the function.
        n = len(num)
        e = (n + 1) // 2          # even-index slots
        o = n // 2                # odd-index slots

        # total sum must be even
        tot_sum = sum(int(c) for c in num)
        if tot_sum % 2 == 1:
            return 0

        # digit counts
        cnt = [0] * 10
        for ch in num:
            cnt[int(ch)] += 1

        # factorials and inverses up to n
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [pow(fact[i], MOD - 2, MOD) for i in range(n + 1)]

        # there are only 10 digits, we can enumerate all x_d efficiently with a 2d DP
        # DP: dp[even_chosen][diff] -> sum of products of inverse factorials
        dp = [defaultdict(int) for _ in range(e + 1)]
        dp[0][0] = 1

        for d in range(10):
            c = cnt[d]
            if c == 0:
                continue
            ndp = [defaultdict(int) for _ in range(e + 1)]
            # iterate over how many copies of digit d go to even positions
            for even_taken in range(e + 1):
                if not dp[even_taken]:
                    continue
                for x in range(c + 1):
                    new_even = even_taken + x
                    if new_even > e:
                        break
                    inv_coeff = (inv_fact[x] * inv_fact[c - x]) % MOD
                    delta = d * (2 * x - c)
                    for diff, ways in dp[even_taken].items():
                        ndp[new_even][diff + delta] = (ndp[new_even][diff + delta]
                                                    + ways * inv_coeff) % MOD
            dp = ndp

        ways_balanced = dp[e].get(0, 0)
        ans = fact[e] * fact[o] % MOD * ways_balanced % MOD
        return ans