def removeInvalidParentheses(s):  # O(2^n) and O(n)
    left = 0
    right = 0
    # First, we find out the number of misplaced left and right parentheses.
    for char in s:
        # Simply record the left one.
        if char == '(':
            left += 1
        elif char == ')':
            # If we don't have a matching left, then this is a misplaced right, record it.
            right = right + 1 if left == 0 else right

            # Decrement count of left parentheses because we have found a right
            # which CAN be a matching one for a left.
            left = left - 1 if left > 0 else left
    result = {}
    def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
        # If we reached the end of the string, just check if the resulting expression is
        # valid or not and also if we have removed the total number of left and right
        # parentheses that we should have removed.
        if index == len(s):
            if left_rem == 0 and right_rem == 0:
                ans = "".join(expr)
                result[ans] = 1
        else:

            # The discard case. Note that here we have our pruning condition.
            # We don't recurse if the remaining count for that parenthesis is == 0.
            if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                recurse(s, index + 1,
                        left_count,
                        right_count,
                        left_rem - (s[index] == '('),
                        right_rem - (s[index] == ')'), expr)

            expr.append(s[index])

            # Simply recurse one step further if the current character is not a parenthesis.
            if s[index] != '(' and s[index] != ')':
                recurse(s, index + 1,
                        left_count,
                        right_count,
                        left_rem,
                        right_rem, expr)
            elif s[index] == '(':
                # Consider an opening bracket.
                recurse(s, index + 1,
                        left_count + 1,
                        right_count,
                        left_rem,
                        right_rem, expr)
            elif s[index] == ')' and left_count > right_count:
                # Consider a closing bracket.
                recurse(s, index + 1,
                        left_count,
                        right_count + 1,
                        left_rem,
                        right_rem, expr)

            # Pop for backtracking.
            expr.pop()

    # Now, the left and right variables tell us the number of misplaced left and
    # right parentheses and that greatly helps pruning the recursion.
    recurse(s, 0, 0, 0, left, right, [])
    return list(result.keys())

def removeInvalidParentheses_alt(s):
    left = right = 0
    for c in s:
        if c == "(":
            left += 1
        elif c == ")":
            if left == 0:
                right += 1
            else:
                left -= 1

    ans = set()

    def dfs(depth, left, right, left_rem, right_rem, cur):
        if depth == len(s):
            if left == right and left_rem == right_rem == 0:
                ans.add(cur)
        else:
            if s[depth] == "(" and left_rem > 0:
                dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
            if s[depth] == ")" and right_rem > 0:
                dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
            if s[depth] != "(" and s[depth] != ")":
                dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])
            elif s[depth] == "(":
                dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")
            elif s[depth] == ")" and right < left:
                dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")

    dfs(0, 0, 0, left, right, "")
    return list(ans)


def removeInvalidParentheses_another(s):
    def backtrack(s, index, current, currentStack, result):
        if index >= len(s):
            if len(currentStack) == 0:
                key = len(current)
                if key in result: result[key].add(current)
                else: result[key] = {current}
            return result
        #Excluding
        if len(currentStack)>=0: self.backtrack(s, index+1, current, currentStack[:], result)
        #Including
        start, bracket = {'(': ')', '{': '}', '[': ']'}, {'(', ')', '{', '}', '[',']'}
        if s[index] in bracket:
            if s[index] in start:
                currentStack.append(s[index])
            elif len(currentStack)==0 or start[currentStack.pop()]!=s[index]:
                return result
        if len(currentStack) >= 0:
            self.backtrack(s, index + 1, current + s[index], currentStack[:], result)
        return result

    dic, maxKey = self.backtrack(s, 0, "", [], {}), 0
        for k in dic:
            if k>maxKey: maxKey = k
        return list(dic[maxKey])


def removeInvalidParentheses_short(s):
    # define when a combination of parenthesis is still valid
    def valid(candidate):
        counter = 0
        for char in candidate:
            if char == "(": counter += 1
            elif char == ")": counter -= 1
            if counter < 0: return False
        # balanced?
        return counter == 0
    # the actual BFS, we return the minimum of removals, so we stop as soon as we have something
    res, frontier = set() , set([s])
    while not res:
        _next = set()
        for candidate in frontier:
            if valid(candidate):
                res.add(candidate)
                continue
            # generate more candidates based on this candidate
            for i, letter in enumerate(candidate):
                if letter not in "()": continue
                _next.add(candidate[:i] + candidate[i+1:])
        frontier = _next
    return res


if __name__ == '__main__':
    print(removeInvalidParentheses('()())()'))
    print(removeInvalidParentheses('a)())()'))
    print(removeInvalidParentheses_alt('()())()'))
    print(removeInvalidParentheses_alt('a)())()'))
