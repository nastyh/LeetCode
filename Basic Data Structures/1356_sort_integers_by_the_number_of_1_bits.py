from collections import defaultdict
from typing import Counter, List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        """
        O(nlogn) both 
        helper create a string: binary representation of a given number
        then sort arr by the key, which builds a binary representation, counts the ones
        and uses the number for sorting purposes 
        """
        def _helper(n):
            if n == 0:
                return '0'
            res = ''
            # takes an integer, returns its bit representation
            while n > 0: 
                res = str(n % 2) + res 
                n //= 2
            return res 

        return sorted(arr, key=lambda num: (_helper(num).count('1'), num))
    
    def sortByBits_longer(self, arr: List[int]) -> List[int]:
        """
        as above w/ extra dicts to preserve the frequencies
        and do step by step
        """
        def _helper(n):
            if n == 0:
                return '0'
            res = ''
            # takes an integer, returns its bit representation
            while n > 0: 
                res = str(n % 2) + res 
                n //= 2
            return res 
         
        freq = Counter(arr) # to preserve the dups

        ones_count = {num: _helper(num).count('1') for num in freq}
        sorted_keys = sorted(ones_count.keys(), key=lambda x: (ones_count[x], x))
        res = []
        for key in sorted_keys:
            res.extend([key] * freq[key])
        return res
    
    def sortByBits_one_liner(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))