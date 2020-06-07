def removeInvalidParentheses(s):
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

if __name__ == '__main__':
    print(removeInvalidParentheses('()())()'))
    print(removeInvalidParentheses('a)())()'))
    print(removeInvalidParentheses_alt('()())()'))
    print(removeInvalidParentheses_alt('a)())()'))
