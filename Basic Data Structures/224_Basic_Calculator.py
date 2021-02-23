def calculate(self, s):  # O(n) both 
    st = []
    operand = 0
    res = 0
    sign = 1
    for ch in s:
        if ch.isdigit():
            operand=(operand * 10) + int(ch)
        elif ch=='+':
            res += sign * operand
            sign = 1
            operand = 0
        elif ch == '-':
            res += sign * operand
            sign =- 1
            operand = 0
        elif ch=='(':
            st.append(res)
            st.append(sign)
            sign = 1
            res = 0
        elif ch == ')':
            res += sign * operand
            res *= st.pop()
            res += st.pop()
            operand = 0
    return res + sign * operand