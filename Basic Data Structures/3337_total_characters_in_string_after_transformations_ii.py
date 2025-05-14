from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        O(s + 26**3 * logT) -- due to the exponentiation
        Space is O(26**2) = O(1)
        due to two or three 26x26 matrices during exponentiation, two length-26 vectors for v_0 
        and the running result 
        """
        MOD, N = 10**9 + 7, 26
        # 1. Build 26×26 transition matrix T
        T = [[0]*N for _ in range(N)]
        for c in range(N):
            for k in range(1, nums[c]+1):
                T[c][(c+k) % N] = 1
        # 2. Fast matrix-exponentiation: T_pow = T^t (mod MOD)
        def mat_mul(A, B):
            C = [[0]*N for _ in range(N)]
            for i in range(N):
                for k in range(N):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(N):
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def mat_pow(M, p):
            R = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
            while p:
                if p & 1: #  bit-wise AND between the integer p and the constant 1
                    """
                    The & operator compares the two numbers bit-by-bit and keeps a 1 only where both have 1
                    p & 1 simply isolates the least-significant bit (the right-most bit):
                    If it equals 1, p is odd and—in the exponentiation-by-squaring loop—this tells us
                    that the current power of the matrix must be multiplied into the result.

                    If it equals 0, p is even and we skip the multiplication for this iteration.
                    """
                    R = mat_mul(R, M)
                M = mat_mul(M, M)
                """
                below
                operator >> is the right-shift (bit-shift) operator.
                It moves every bit in the binary representation of p one position to the right.
                the same as integer-dividing by 2 and taking the floor.
                """
                p >>= 1
            return R

        T_pow = mat_pow(T, t)

        # 3. Count initial letters
        v0 = [0]*N
        for ch in s:
            v0[ord(ch) - 97] += 1

        # 4. v_t = v0 · T_pow   (vector–matrix product)
        v_t = [0]*N
        for j in range(N):
            total = 0
            for k in range(N):
                total = (total + v0[k] * T_pow[k][j]) % MOD
            v_t[j] = total

        # 5. Total length is the sum of all entries
        return sum(v_t) % MOD