class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        O(n) both 
        palindrome as a number where the first half is mirrored to create the second half
        edge cases:
        odd-lengths of numbers
        so we need to
        Palindrome formed from the first half of n.
        Palindrome formed from the first half decremented by 1.
        Palindrome formed from the first half incremented by 1.
        Nearest palindrome of the form 99, 999, etc.
        Nearest palindrome of the form 101, 1001, etc.
        """
        l, candidates = len(n), set()
        if n == '1': return '0'
        # basic palindrome by mirroring the left side
        prefix = n[:(l+1)//2]
        prefix_num = int(prefix)

        # generate the candidates
        for i in [-1, 0, 1]:
            new_prefix = str(prefix_num + i)
            if l % 2 == 0:
                candidate = new_prefix + new_prefix[::-1] # portion + mirrored version
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)

        """
        Adding edge cases: smallest palindrome larger than current number of digits, and largest palindrome smaller
        than the current number of digits
        """
        candidates.add(str(10**(l-1) - 1))
        candidates.add(str(10**l + 1))

        candidates.discard(n)
        res = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        return res