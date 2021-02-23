from collections import deque
def calculate(s):
    def _helper(self,q):
        stack = []
        num = ''
        sign = '+'
        while q:
            x = q.popleft()
            if x == '(':
                num = self._helper(q)
            if x.isnumeric():
                num += x
            if not x.isnumeric() or not q:
                if sign =='+':
                    stack.append(int(num or 0))
                elif sign == '-':
                    stack.append(-1 * int(num or 0))
                elif sign == '*':
                    stack.append(stack.pop() * int(num) )
                elif sign == '/':
                    stack.append(int(stack.pop() / int(num)))
                sign = x
                num = ''
            if x== ')':
                break
        return sum(stack)

    q=deque(s.replace(' ',''))
    return self.helper(q)


    
    