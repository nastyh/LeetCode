from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        """
        O(n) to iterate twice
        O(n) for storing original
        XOR is reversible
        a xor b = c
        a = c xor b
        b = c xor a
        derived[i] = original[i] xor original[i+1] for i in [0, n - 2]
        derived[n-1] = original[n-1] xor original[0]
        Two ways to reconstruct original
        assume original[0] = 0 and compute the rest of original
        assume original[0] = 1 and compute the rest of original
        after computing original, final computed original[0] == assumed original[0]
        """
        n = len(derived)
        def _helper(start):
            original = [0] * n
            original[0] = start
            for i in range(1, n):
                original[i] = derived[i - 1] ^ original[i - 1]
            # Check circular condition
            return (original[n - 1] ^ original[0]) == derived[n - 1]

        return _helper(0) or _helper(1)