from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """
        O(n+value), to compute residues, update see. O(value) to find the mex
        O(value) for the seen list
        Any number in the array can be transformed into a residue modulo (n mod value) via + or - of multiples of value
        The goal is to ensure that all possible residues [0, 1, value - 1] are covered as much as possible
        We can focus on tracking which residues modulo value exist in the list
        maintain a set or a boolean list of residues present in the array modulo value
        """
        seen = [0] * value
        # Count occurrences of residues modulo `value`
        for num in nums:
            residue = (num % value + value) % value  # Ensure non-negative residue
            seen[residue] += 1
        # Find the MEX by simulating the smallest missing integer
        mex = 0
        while seen[mex % value] > 0:
            seen[mex % value] -= 1
            mex += 1
        
        return mex