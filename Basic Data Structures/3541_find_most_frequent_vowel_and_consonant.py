from typing import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        """
        O(n) to process the string
        O(1) since the dictionaries will contain 26 elements at most 
        Do what is asked
        Set of vowels for a quick check
        Build two dictionaries with frequencies 
        Find the max frequencies from each, sum them up, return
        Edge case if if one of the dicts is empty, thus, we have to add this if len(...) check 
        """
        res_v, res_c = 0, 0
        vowels = set()
        vowels = {ch for ch in 'aeiou'}
        d_v, d_c = dict(), dict()
        for ch in s: 
            if ch in vowels: 
                if ch not in d_v:
                    d_v[ch] = 1
                else:
                    d_v[ch] += 1 
            else:
                if ch not in d_c:
                    d_c[ch] = 1
                else:
                    d_c[ch] += 1
        # if len(d_v) > 0: 
        #     res_v = max(d_v.values())
        # if len(d_c) > 0:
        #     res_c = max(v for v in d_c.values())
        # can be simplified as 
        # return res_v + res_c
        return (max(d_c.values()) if d_c else 0) + (max(d_v.values()) if d_v else 0)
    
    def maxFreqSum_one_liner(self, s: str) -> int:
       return sum(max([*Counter(c for c in s if (c in 'aeiou')^q).values(),0]) for q in (0,1)) 