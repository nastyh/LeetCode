def numDecodings(s):  # O(n) and O(n)
    if s == '0': return 0
    if len(s) == 1: 
        return len(s)
    dp = [0] * (len(s) + 1)
    dp[0] = 1  # there is one way to decode a string that has no elements at all (like not to decode at all and it counts as 1)
    if s[0] == '0':
        dp[1] = 0
    else:
        dp[1] = 1
    for ix in range(2, len(s) + 1):
        if int(s[ix - 1 : ix]) >= 1:
            dp[ix] += dp[ix - 1]
        if 26 >= int(s[ix - 2 : ix]) >= 10:
            dp[ix] += dp[ix - 2]
    return dp[-1]


def numDecodings_top_down(s):
    def _helper(s, memo):
        if not s: # We reached an answer here
            return 1
        if s[0] == "0":  # Any # with 0 at start of string is invalid, including 0 itself
            return 0
        if s in memo: # Retrieve from cache
            return memo[s]
        res = 0
        res += _helper(s[1:], memo)
        if len(s) >= 2:
            if int(s[0:2]) <= 26: # Check if the first 2 numbers are over 26. Then recursively call the function on the rest of the string
                res += _helper(s[2:], memo)
        memo[s] = res
        return memo[s]
    return _helper(s, {})


def numDecodings_constant_space(s):  # O(n) and O(1):
    """
    To calculate the i-th element, we need to know i-2nd and i-1st
    """
    if s[0] == "0":
        return 0
    two_back = 1
    one_back = 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != "0":
            current = one_back
        two_digit = int(s[i - 1: i + 1])
        if two_digit >= 10 and two_digit <= 26:
            current += two_back
        two_back = one_back
        one_back = current
    
    return one_back


if __name__ == '__main__':
    print(numDecodings('226'))
    print(numDecodings_top_down('226'))