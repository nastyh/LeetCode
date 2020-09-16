from collections import defaultdict
def getHint(secret, guess):  # slow and takes space but passes
    res = []
    bull, cow = 0, 0
    toremove = []
    for ix in range(len(secret)):
        if secret[ix] == guess[ix]:
            bull += 1
            toremove.append(ix)
    sl, gl = defaultdict(list), defaultdict(list)
    for k, v in enumerate(secret):
        if k not in toremove:
            sl[v].append(k)
    for k, v in enumerate(guess):
        if k not in toremove:
            gl[v].append(k)
    for k in sl.keys():
        if k in gl.keys():
            cow += 1 * min(len(gl[k]), len(sl[k]))
    #return f'{bull}A{cow}B'  # a straightforward way to return the result
    res.append(str(bull))
    res.append('A')
    res.append(str(cow))
    res.append('B')
    return ''.join(i for i in [str(i) for i in res]) 


if __name__ == "__main__":
    print(getHint('1807', '7810'))
    print(getHint('1122', '2211'))
    print(getHint('1123', '0111'))
