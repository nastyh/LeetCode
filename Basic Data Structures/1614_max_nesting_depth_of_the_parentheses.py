class Solution:
    def maxDepth(self, s: str) -> int:
        res, op = 0, 0
        # if opening, increment op,
        # result is the max of what we've seen and op
        # if closing, decrement op, since we just closed a pair
        for element in s:
            if element == '(':
                op += 1
                res = max(res, op)
            elif element == ')':
                op -= 1
        return res