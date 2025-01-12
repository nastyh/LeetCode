class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        """
        O(n) to traverse
        O(1)
        Keep track of the balance of parentheses (opens)
        for each char check:
        if it's ( or unlocked is 0, increase opens
        if ) and locked, decrease opens 
        if becomes < 0, False
        One more pass from right to left 
        if ) or locked is 0, increase closed
        else: decrease
        if becomes < 0, False
        finally True 
        """
        if len(s) % 2 == 1: return False
        opens = 0 
        closed = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                opens += 1
            else:
                opens -= 1
            if opens < 0:
                return False
        for i in range(len(s) -1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                closed += 1
            else:
                closed -= 1
            if closed < 0:
                return False
        return True
            