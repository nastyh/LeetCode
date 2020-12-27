from collections import defaultdict
def repeatedSubstringPattern_brute_force(s):  # O(n^2)
    for n in range(1, len(s)//2 + 1):
        if len(s) % n == 0 and s == s[:n] * (len(s)//n):
            return True
    return False

def repeatedSubstringPattern_another(s):
    """
    Generate substrings and check if (appropriate number of) repeatitions of those substrings leads to original string.
    """
    sub_str, l = "", len(s)
    for i in range(l//2, 0, -1):
        if l % i == 0:
            num_repeats = l // i
            sub_str = (s[0:i]) * num_repeats
            if sub_str == s: return True
    return False


def repeatedSubstringPattern_KMP(s):
    n = len(s)
    dp = [0] * n
    for i in range(1, n):
        j = dp[i - 1]
        while j > 0 and s[i] != s[j]:
            j = dp[j - 1]
        if s[i] == s[j]:
            j += 1
        dp[i] = j

    l = dp[n - 1]
    # check if it's repeated pattern string
    return l != 0 and n % (n - l) == 0



def repeatedSubstringPattern(s):  # fail
    values, diff = [], []
    if len(s) % 2 == 1: return False
    d = defaultdict(list)
    for k, v in enumerate(s):
        d[v].append(k)
    for v in d.values():
        # if any(num == 1 for num in v):
        #     return False
        # else:
        if len(v) == 1:
            return False
        else:
            values.append(v)  # [[0, 2, 5], [1, 3, 4]]
    for element in values:
        for ix in range(len(element) - 1):
            diff.append(element[ix + 1] - element[ix])  # [2, 3, 2, 1]
    # return len(set(diff)) == 1
    return diff


def repeatedSubstringPattern_alt(s):  # fail
    values, diff = [], []
    if len(s) % 2 == 1: return False
    d = defaultdict(list)
    for k, v in enumerate(s):
        d[v].append(k)
    for v in d.values():
        if len(v) == 1:
            return False
        else:
            values.append(v)
    for element in values:
        temp = []
        for ix in range(len(element) - 1):
            temp.append(element[ix + 1] - element[ix])
        diff.append(temp)
    res = []
    for l in diff:
        res.append(sum(l))
    return len(set(res)) == 1


if __name__ == '__main__':
    # print(repeatedSubstringPattern('abab'))
    # print(repeatedSubstringPattern('aba'))
    # print(repeatedSubstringPattern('abcabcabcabc'))
    # print(repeatedSubstringPattern('ababba'))
    # print(repeatedSubstringPattern('abac'))
    # print(repeatedSubstringPattern('abaababaab'))
    print(repeatedSubstringPattern_alt('abab'))
    print(repeatedSubstringPattern_alt('aba'))
    print(repeatedSubstringPattern_alt('abcabcabcabc'))
    print(repeatedSubstringPattern_alt('ababba'))
    print(repeatedSubstringPattern_alt('abac'))
    print(repeatedSubstringPattern_alt('abaababaab'))
    print(repeatedSubstringPattern_alt('abacababacab'))
    
     