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
    for letter in s:
        if letter not in ss:
            ss.add(letter)
        else:
            ss.remove(letter)
    if len(ss) != 0:
        return len(s) - len(ss) + 1
    else:
        return len(s)


if __name__ == '__main__':
    print(longestPalindrome('abccccdd'))
    print(longestPalindrome('a'))
    print(longestPalindrome('bb'))
    print(longestPalindrome('bananas'))
    print(longestPalindrome_set('abccccdd'))
    print(longestPalindrome_set('a'))
    print(longestPalindrome_set('bb'))
    print(longestPalindrome_set('bananas'))