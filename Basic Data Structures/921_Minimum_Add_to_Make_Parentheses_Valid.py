def minAddToMakeValid(S):  # O(n) both 
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
        if ch == '(':
            stack.append(ch)
        else:
            if stack and stack[-1] == '(':  # mean a legit pair
                stack.pop()
            else: stack.append(ch)  # append whatever 
    return len(stack)


def minAddToMakeValid_alt(s): # easier to understand
    if len(set(s)) == 1: return len(s)
    if len(s) == 0: return 0
    st, counter = [], 0
    for ch in s:
        if ch == '(': # add only opening into the stack
            st.append(ch)
        else: # once you see the closing
            if len(st) != 0:
                st.pop() # if there is at least one opening stored, then there is a pair, so remove the opening and move on
            else:
                counter += 1 # if no opening in the stack, count this closing, b/c it will need a pair
    return len(st) + counter # return the sum: all opening that are in the stack and are not matched and/or all closing if any

if __name__ == '__main__':
    print(minAddToMakeValid('())'))
    print(minAddToMakeValid('()'))
    print(minAddToMakeValid('()))(('))
    # print(minAddToMakeValid_stack('())'))
    # print(minAddToMakeValid_stack('()'))
    # print(minAddToMakeValid_stack('()))(('))
    print(minAddToMakeValid_alt('())'))
    print(minAddToMakeValid_alt('()'))
    print(minAddToMakeValid_alt('()))(('))
