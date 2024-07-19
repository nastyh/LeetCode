class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        O(n) both
        """
        stack = []
        for char in s:
            if char == ')':
                temp = []  # saving what's in the current () portion
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(char)
        return ''.join(stack)