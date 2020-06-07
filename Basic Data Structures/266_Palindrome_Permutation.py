from collections import Counter
def canPermutePalindrome(s):
    s_d = Counter(s)
    if sum([1 for i in s_d.values() if i % 2 == 1]) > 1:
        return False
    else:
        return True
    # if we have more than one key with the odd value, then it's not a palindrome

if __name__ == '__main__':
    print(canPermutePalindrome('carerac'))
    print(canPermutePalindrome('code'))
    print(canPermutePalindrome('aab'))
