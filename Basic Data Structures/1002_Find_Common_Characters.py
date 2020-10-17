from collections import Counter
def commonChars(A):
    A.sort(key = lambda x: len(x))
    d_shortest = Counter(A[0])
    for word in A[1:]:
        for k in d_shortest:
            d_shortest[k] = min(d_shortest[k], word.count(k))
    res = []
    for k, v in d_shortest.items():
        if v >= 1:
            for _ in range(v):
                res.append(k)
    return res


if __name__ == '__main__':
    print(commonChars(["bella","label","roller"]))