import string
from collections import Counter
def mostCommonWord(paragraph, banned):

    for c in string.punctuation:
            paragraph = paragraph.replace(c,'')

    p = [i.lower() for i in paragraph.strip().split(' ')]
    d = Counter(p)
    for x in banned:
        del d[x]
    return sorted(d, key = d.get, reverse = True)[0]


if __name__ == '__main__':
    print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
