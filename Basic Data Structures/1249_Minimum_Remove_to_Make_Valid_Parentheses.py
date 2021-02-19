def minRemoveToMakeValid_myself(s):  # O(n) both
    """
    We'll do two passes to collect indices of elements that we want to remove
    First pass from left to right to catch unwanted closing parentheses
    Second pass from right to left to catch unwanted opening parentheses
    """
    candidates, st_closing, st_opening, res = set(), [], [], ''
    for k, v in enumerate(s):
        if v == ')':
            if len(st_closing) == 0:  # definitely a bad parenthesis
                candidates.add(k)
            else:
                st_closing.pop()  # it means that this closing parenthesis pairs well with an opening parenthesis that happened earlier
        if v == '(':
            st_closing.append(v)  # just building our stack
            
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            if len(st_opening) == 0:   # definitely a bad parenthesis
                candidates.add(i)
            else:
                st_opening.pop()   # it means that this opening parenthesis pairs well with an closing parenthesis that happened earlier
        if s[i] == ')':
            st_opening.append(s[i])   # just building our stack
            
    for k, v in enumerate(s):
        if k not in candidates:  # using set() for candidates allows us to make the program faster
            res += v
    return res


def minRemoveToMakeValid(s):
    indexes_to_remove = set()
    stack = []
    for i, c in enumerate(s):
        if c not in "()":
            continue
        if c == "(":
            stack.append(i)
        elif not stack:
            indexes_to_remove.add(i)
        else:
            stack.pop()
    indexes_to_remove = indexes_to_remove.union(set(stack))
    string_builder = []
    for i, c in enumerate(s):
        if i not in indexes_to_remove:
            string_builder.append(c)
    return "".join(string_builder)


def minRemoveToMakeValid_alt(s):
    first_parse_chars = []
    balance = 0
    open_seen = 0
    for c in s:
        if c == "(":
            balance += 1
            open_seen += 1
        if c == ")":
            if balance == 0:
                continue
            balance -= 1
        first_parse_chars.append(c)

    # Parse 2: Remove the rightmost "("
    result = []
    open_to_keep = open_seen - balance
    for c in first_parse_chars:
        if c == "(":
            open_to_keep -= 1
            if open_to_keep < 0:
                continue
        result.append(c)

    return "".join(result)


if __name__ == '__main__':
    # print(minRemoveToMakeValid_bad('lee(t(c)o)de)'))
    # print(minRemoveToMakeValid_bad('a)b(c)d'))
    # print(minRemoveToMakeValid_bad('))((')) #check it
    # print(minRemoveToMakeValid_bad('(a(b(c)d)'))
    # print(minRemoveToMakeValid_bad('a)b(c)d'))
    print(minRemoveToMakeValid('lee(t(c)o)de)'))
    print(minRemoveToMakeValid('a)b(c)d'))
    print(minRemoveToMakeValid('))(('))
    print(minRemoveToMakeValid('(a(b(c)d)'))
    print(minRemoveToMakeValid('a)b(c)d'))
    print(minRemoveToMakeValid_alt('lee(t(c)o)de)'))
    print(minRemoveToMakeValid_alt('a)b(c)d'))
    print(minRemoveToMakeValid_alt('))(('))
    print(minRemoveToMakeValid_alt('(a(b(c)d)'))
    print(minRemoveToMakeValid_alt('a)b(c)d'))

