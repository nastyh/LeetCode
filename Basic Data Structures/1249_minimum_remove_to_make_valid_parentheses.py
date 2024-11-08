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

    def minRemoveToMakeValid_no_stack(self, s: str) -> str:
        """
        Initialize pointers for the start and end of the string, variables to
        store the start and end parts of the string, and the final result
        Iterate through the string from left to right. Track the count of open parentheses encountered.
        If an excess closing parenthesis is encountered (i.e., a closing parenthesis with no matching opening parenthesis),
        mark it with '*'. Keep track of the count of open parentheses encountered.
        Filter out the marked characters ('*') from the character array, leaving only the valid parentheses.
        Construct the result string from the filtered character array.
        Return the final result string, which contains the minimum number of parentheses required to make the input string valid.
        O(n) both
        """
        openParenthesesCount = 0
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == '(':
                openParenthesesCount += 1
            elif arr[i] == ')':
                if openParenthesesCount == 0:
                    arr[i] = '*' # Mark excess closing parentheses
                else:
                    openParenthesesCount -= 1
        for i in range(len(arr) - 1, -1, -1):
            if openParenthesesCount > 0 and arr[i] == '(':
                arr[i] = '*' # Mark excess opening parentheses
                openParenthesesCount -= 1
        result = ''.join(c for c in arr if c != '*')
        return result