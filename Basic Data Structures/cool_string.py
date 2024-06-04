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
        n.sort() # going up
        if len(n) < 2:
            res = True   
        elif len(n) == 2: # if the length of list is 2 and the 1st value in the is 1 then the result will be true 
            if n[0] == 1:
                res = True
            if n[1] - n[0] == 1:   #if the length of list is 2 and the difference between between the 2nd and the 1st value(n[1]-n[0]) is 0 then the result will be true
                res = True
        else:
            if n[0] == 1 and n[1] == n[-1]:   #if the list size is greater than 2, and sortingthe 1st value is 1(n[0]==1) and the remaining values in the list are equal then the result will be true
                res = True 
            if n[0] == n[-2] and n[-1]-n[-2] == 1:  #if the list size is greater than 2, and if all the values in the list are equal and the difference between last 2 values(n[-1]-n[-2]) is 1 then the result is 1`
                res = True
        return res

            

