from collections import Counter
def pluralize_pythonic(words):
    res, d = [], Counter(words)
    res.append([k + 's' if v > 1 else k for k, v in d.items()])    
    return res[0]


def pluralize_straigthforward(words):
    res = []
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    for k, v in d.items():
        if v > 1:
            res.append(k + 's')
        else:
            res.append(k)
    return res 

if __name__ == '__main__':   
    print(pluralize_pythonic(['cow', 'pig', 'cow', 'cow']))
    print(pluralize_pythonic(['table', 'table', 'table']))
    print(pluralize_pythonic(['chair', 'pencil', 'arm']))
    print(pluralize_straigthforward(['cow', 'pig', 'cow', 'cow']))
    print(pluralize_straigthforward(['table', 'table', 'table']))
    print(pluralize_straigthforward(['chair', 'pencil', 'arm']))