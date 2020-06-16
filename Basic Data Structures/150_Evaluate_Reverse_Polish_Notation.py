import math
def evalRPN(tokens):
    st, res = [], 0
    for token in tokens:
        if token not in ['*','/','-','+']:
            st.append(token)
        else:
            num2 = int(st.pop())
            num1 = int(st.pop())
            if token == '+':
                st.append(num1 + num2)
            elif token == '-':
                st.append(num1 - num2)
            elif token == '*':
                st.append(num1 * num2)
            elif token == '/':
                if num1 / num2 < 0:
                    st.append(math.ceil(num1 / num2))
                else:
                    st.append(num1 // num2)
    return st[0]

if __name__ == '__main__':
    print(evalRPN(["2", "1", "+", "3", "*"]))
    print(evalRPN(["4", "13", "5", "/", "+"]))
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

