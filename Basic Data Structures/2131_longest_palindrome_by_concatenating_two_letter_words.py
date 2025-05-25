from typing import Counter, List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        O(n) both
        n num of words
        process the words once
        build a dictionary of words

        A palindrome is symmetric around its center.
        For two-character strings:
        If the string is like "ab", we need its reverse "ba" to form a palindrome
        If the string is like "aa" (same characters), it can be placed in the center or in mirrored pairs.

        Count all word frequencies.
        For asymmetric pairs (e.g., "ab" and "ba"), pair them up as many times as possible.
        For symmetric words (e.g., "cc"), pair them up and optionally use one unpaired symmetric word in the center.
        """
        d = Counter(words)
        res, used_center = 0, False
        for word in list(d.keys()):
            rev = word[::-1]
            if word != rev: # the word is not a palindrome itself: ab 
                pairs = min(d[word], d[rev]) # ensures we don't overuse either word
                res += pairs * 4 # Each pair contributes 4 characters to the final palindrome: ab+ba = abba or baab--> 4 chars
                d[word] -= pairs # decrement the counts accordingly
                d[rev] -= pairs # decrement the counts accordingly
            else: # symmetric: gg
                pairs = d[word] // 2 # can pair two "aa"s into something like "aaaa" (a palindrome). How many pairs we can form
                res += pairs * 4 # Each such pair adds 4 characters 
                d[word] -= pairs * 2 # remove those used pairs
 
        # If there's any leftover "aa"/"cc"/etc., and we've already built both "sides" 
        for word in d:
            if word[0] == word[1] and d[word] > 0:
                res += 2 # can place one symmetric word in the center; adds 2 characters to the total palindrome length.
                break # can only use one such leftover symmetric word in the center 
        return res