class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # two passes: left to right and other way around
        # first time: if it's closing and nothing in the list, it is a candidate
        # if it's closing and there something in the list, pop it since it's opening, and we have a pair
        # if it's opening, just add
        # second pass from the right
        # if it's opening and nothing in the list, it's a candidate
        # if it's opening and something in the list, it's a pair, pop 
        # if it's closing, just add 
        # you have a list with indices that you don't want in the result
        # construct the result 
        candidates, st_open, st_close, res = set(), [], [], ''
        for k, v in enumerate(s):
            if v == ')':
                if len(st_close) == 0: 
                    candidates.add(k)
                else:
                    st_close.pop()
            if v == '(':
                st_close.append(v)
        for i in range(len(s) - 1, -1 , -1):
            if s[i] == '(':
                if len(st_open) == 0:
                    candidates.add(i)
                else:
                    st_open.pop()
            if s[i] == ')':
                st_open.append(s[i])
        for k, v in enumerate(s):
            if k not in candidates:
                res += v
        return res