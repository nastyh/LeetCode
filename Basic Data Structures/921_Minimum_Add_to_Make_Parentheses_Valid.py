def minAddToMakeValid(S):
    if len(set(S)) == 1: return len(S)
    if len(S) == 0: return 0
    opening, closing = 0, 0
    for ch in S:
        if ch == '(':
            opening += 1
        else:
            if opening == 0:
                closing += 1
            else:
                opening -= 1
    return opening + closing

def minAddToMakeValid_stack(S):
    stack = []
    for ch in S:
        if ch == '(': stack.append(ch)
        else:
            if len(stack) and stack[-1] == '(': stack.pop()
            else: stack.append(ch)
    return len(stack)

if __name__ == '__main__':
    print(minAddToMakeValid('())'))
    print(minAddToMakeValid('()'))
    print(minAddToMakeValid('()))(('))
    print(minAddToMakeValid_stack('())'))
    print(minAddToMakeValid_stack('()'))
    print(minAddToMakeValid_stack('()))(('))
