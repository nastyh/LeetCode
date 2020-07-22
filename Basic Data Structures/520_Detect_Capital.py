def detectCapitalUse(word):
    if word == word.lower(): return True
    if word == word.upper(): return True
    if all([i.isupper() for i in word[0]]) and all(i.islower() for i in word[1:]): return True
    return False 


if __name__ == '__main__':
    print(detectCapitalUse('USA'))
    print(detectCapitalUse('FlaG'))
    print(detectCapitalUse('Leetcode'))
    