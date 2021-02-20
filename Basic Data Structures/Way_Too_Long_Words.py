"""
https://codeforces.com/problemset/problem/71/A
"""
def way_too_long(word):
    res = ''
    if len(word) <= 10:
        return word
    res += word[0] + str(len(word[1:-1])) + word[-1]
    return res


if __name__ == '__main__':
    print(way_too_long('word'))
    print(way_too_long('localization'))
    print(way_too_long('internationalization'))
    print(way_too_long('pneumonoultramicroscopicsilicovolcanoconiosis'))
