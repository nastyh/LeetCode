from collections import Counter
def canPermutePalindrome(s):
    s_d = Counter(s)
    if sum([1 for i in s_d.values() if i % 2 == 1]) > 1:
        return False
    else:
        return True
    # if we have more than one key with the odd value, then it's not a palindrome


def canPermutePalindrome_alt(s):  # same idea but with a set
    chars = set()
    for ch in s:
        if( ch in chars):
            chars.remove(ch)
        else:
            chars.add(ch)
    return len(chars) <= 1

if __name__ == '__main__':
    # print(canPermutePalindrome('carerac'))
    # print(canPermutePalindrome('code'))
    # print(canPermutePalindrome('aab'))
    print(canPermutePalindrome_alt('carerac'))
    print(canPermutePalindrome_alt('code'))
    print(canPermutePalindrome_alt('aab'))
