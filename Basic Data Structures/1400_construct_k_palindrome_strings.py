from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        O(n)
        O(1) since the dict has 26 keys at most 
        1 char is a palindrome
        all even frequencies is a palindrome: aabb --> abba
        one odd frequency (in the middle), others even: aabbc --> bbcaa

        Even counts can be distributed --> don't affect the num of palindromes
        we can build
        Odd counts have to appear in the middle of a palindrome
        Thus, the num of odd counts defines how many palindromes we can have
        if the number of odd-frequency characters is greater than k, it’s impossible to form k palindromes
        If it's <= k, then True
        """
        if len(s) < k: return False # edge case
        d = Counter(s)
        num_of_odd_counts = 0
        for v in d.values():
            if v % 2 == 1:
                num_of_odd_counts += 1
        if num_of_odd_counts > k: 
            return False
        else: 
            return True