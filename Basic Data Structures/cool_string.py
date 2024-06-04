class Solution:
    def cool_string(self, word: str) -> bool:
        """
        all letters have the same frequency
        or only one have a count that is one more
        """
        res = False
        d = Counter(word)
        n = []
        for v in d.values():
            n.append(v)
        n.sort()
        if len(n) < 2:
            res = True   
        elif len(n) == 2: # if the length of list is 2 and the 1st value in the is 1 then the result will be true 
            if n[0] == 1:
                res = True
            if n[1] - n[0] == 1:
                res = True
        else:
            if n[0] == 1 and n[1] == n[-1]:
                res = True 
            if n[0] == n[-2] and n[-1]-n[-2] == 1:
                res = True
        return res

            

