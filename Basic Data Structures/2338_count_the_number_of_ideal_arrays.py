import math
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        O(maxValue * log(maxValue))
        O(maxValue * L) for the dp table or O(maxValue) for rolling arrays
        O(n) for factorial tables 
        Any strictly increasing chain of divisors ending at a num <=maxValue can 
        have length at most
        L = 1 + log2(maxValue)
        because each step in a strictly increasing divisor chain must at least double the value.
        An ideal array of length n can be thought of as choosing a strictly increasing “backbone” of l (1<=l<=L) distinct values 
        and then “stretching” each of these l values over a contiguous block so that the total length is n.
        """
        MOD = 10**9 + 7
        res = 0
        # 1. Precompute divisors for each v
        divisors = [[] for _ in range(maxValue+1)]
        for d in range(1, maxValue+1):
            for multiple in range(d, maxValue+1, d):
                divisors[multiple].append(d)
        
        # 2. Determine max chain length L
        L = math.floor(math.log2(maxValue)) + 1

        # 3. DP: f[l][v] = # of strictly increasing divisor‑chains of length l ending at v
         #  only need two layers at once
        f = [[0] * (maxValue+1) for _ in range(L+1)]
        # Base: length‑1 chain
        for v in range(1, maxValue+1):
            f[1][v] = 1
        # Fill for l = 2..L
        for length in range(2, L+1):
            for v in range(1, maxValue+1):
                total = 0
                # sum over all proper divisors u < v
                for u in divisors[v]:
                    if u < v:
                        total += f[length-1][u]
                f[length][v] = total % MOD
        # 4. Sum up S_l = sum_v f[l][v]
        S = [0] * (L+1)
        for l in range(1, L+1):
            S[l] = sum(f[l][1:]) % MOD
        # 5. Precompute factorials & inv-factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv = [1] * (n + 1)
        inv[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inv[i-1] = inv[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a: 
                return 0
            return fact[a] * inv[b] % MOD * inv[a-b] % MOD

        # 6. Combine
        for l in range(1, L+1):
            res = (res + S[l] * comb(n-1, l-1)) % MOD
        
        return res 