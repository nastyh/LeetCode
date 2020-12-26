def numDecodings(s):
    one = {str(i): 1 for i in range(1, 10)}
    one.update({'*': 9, '0': 0})
    two = {str(i): 1 for i in range(10, 27)}
    two.update({'*' + str(i): 2 if i <= 6 else 1 for i in range(10)})
    two.update({'1*': 9, '2*': 6, '**': 15})
    dp = (1, one.get(s[:1], 0))

    for i in range(1, len(s)):
        dp = (dp[1], (one.get(s[i]) * dp[1] + two.get(s[i - 1: i + 1], 0) * dp[0]) % 1000000007)

    return dp[-1]
    

def numDecodings_alt(s):
    answer = 1
    prev_answer = 1
    # the prev value is 1, 2 or not
    one, two = False, False
    for i in S:
        if i == '*':
            new = answer * 9
            if one:
                new += 9 * prev_answer
            if two:
                new += 6 * prev_answer
            one, two = True, True
        else:
            # drop it if meet 0
            new = answer if (i > '0') else 0
            if one:
                new += prev_answer
            if (two and i <= '6'):
                new += prev_answer
            one = (i == '1')
            two = (i == '2')
        prev_answer = answer
        answer = new % (10**9 + 7)
    return answer