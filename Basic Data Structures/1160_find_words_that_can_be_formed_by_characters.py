class Solution:
    def countCharacters_pythonic(self, words: List[str], chars: str) -> int:
        """
        O(n + m*k), n length of chars, m -- total length of words, k -- average length of a word
        O(1) since each dict is no bigger than 26 elements 
        The q is poorly worded. Actually for each word you can use everything in chars
        from scratch.
        As such, we can build a dict for each word and compare it to the original dict.
        If everything matches, it means a given word can be created, thus, add its length
        to res 
        """
        d = Counter(chars)
        res = 0
        for word in words:
            word_d = Counter(word)
            if word_d <= d:
                res += len(word)
        return res

    def countCharacters_another(self, words: List[str], chars: str) -> int:
        """
        less pythonic
        build both dict
        take elements and frequencies from the word dict and check that d[element] >= frequency
        if no, stop the loop
        need a boolean for this. it's mark
        if all good, add the word's length to res
        """
        d = Counter(chars)
        res = 0
        for word in words: 
            word_d = Counter(word)
            mark = True
            for ch, freq, in word_d.items():
                if d[ch] < freq:
                    mark = False
                    break
            if mark:
                res += len(word)
        return res