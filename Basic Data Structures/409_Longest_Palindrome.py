from collections import Counter
def longestPalindrome(s):
    dic = {}
    for i in s:
        if i in dic:
            del dic[i]
        else:
            dic[i] = 1
    if not dic :
        return len(s)
    return len(s) - len(dic) + 1
    

def longestPalindrome_set(s):
    ss = set()
    # set contains letters that have odd frequency
    for letter in s:
        if letter not in ss:
            ss.add(letter)
        else:
            ss.remove(letter)
    if len(ss) != 0:
        return len(s) - len(ss) + 1
    else:
        return len(s)


def longestPalindrome_greedy(s):
    ans = 0
    d = Counter(s)
    for v in d.values():
        ans += v // 2 * 2
        if ans % 2 == 0 and v % 2 == 1:
            ans += 1
    return ans


if __name__ == '__main__':
    print(longestPalindrome('abccccdd'))
    print(longestPalindrome('a'))
    print(longestPalindrome('bb'))
    print(longestPalindrome('bananas'))
    print(longestPalindrome_set('abccccdd'))
    print(longestPalindrome_set('a'))
    print(longestPalindrome_set('bb'))
    print(longestPalindrome_set('bananas'))
