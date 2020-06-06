def minRemoveToMakeValid(s):
    stack, opened, closed = [], 0, 0
    for c in s:
        if c == '(':
            opened += 1
            stack.append(c)
        elif c == ')':
            if closed < opened:
                closed += 1
                stack.append(c)
        else:
            stack.append(c)

    res, opened, closed = "", 0, 0
    while stack:
        c = stack.pop()
        if c == '(':
            if opened < closed:
                opened += 1
                res = c + res
        elif c == ')':
            closed += 1
            res = c + res
        else:
            res = c + res
    return res

def minRemoveToMakeValidSol2(s):
    st = []
    res = [c for c in s]
    for i in range(len(s)):
        if s[i] == '(':
            st.append(i)
        elif s[i] == ')':
            if st:
                st.pop()
            else:
                res[i] = '#'
    while st:
        res[st.pop()] = '#'

    return "".join(res).replace("#", "")


if __name__ == '__main__':
    print(minRemoveToMakeValid("lee(t(c)o)de)"))
    print(minRemoveToMakeValidSol2("lee(t(c)o)de)"))
