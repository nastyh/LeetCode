def scoreOfParentheses(S):  # O(n) both
    stack = []
    cur, prev = 0, 0
    # scan each symbol in stack
    for char in S:
        if char == '(':
            # '(', push in with current socre
            stack.append(cur)
            # reset previous and current to zero
            prev, cur = 0, 0
        else:
            # ')' match with latest '(', get top score
            top = stack.pop()
            if prev:
                # we have valid parenthesis pair inside, add prev
                cur += top + prev
            else:
                # no parenthesis pair inside, directly add 1
                cur += top + 1
        # update previous as current
        prev = cur
    # total score so far
    return cur


def scoreOfParentheses_recursively(S):
    if not S: return 0
    pos = 0
    def nested():
        nonlocal S, pos
        tempVal = 0
        while pos < len(S):
            if S[pos] == '(':
                pos += 1
                val = nested()
                if val == 0:
                    tempVal += 1
                tempVal += 2 * val
            else:
                pos += 1
                return tempVal
        return tempVal
    return nested()