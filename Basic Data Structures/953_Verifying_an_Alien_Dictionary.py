def isAlienSorted(words, order):

        def _helper(left, right, d):

            for l_ix in range(min(len(left), len(right))):
                if d[left[l_ix]] > d[right[l_ix]]:
                    return False
                elif d[left[l_ix]] < d[right[l_ix]]:
                    return True
                else:
                    continue
            return True if len(left) < len(right) else False

        d = {}
        for k, v in enumerate(order):
            if v not in d:
                d[v] = k

        isSorted = False
        for w_ix in range(len(words) - 1):
            isSorted = _helper(words[w_ix], words[w_ix + 1], d)
            if not isSorted:
                return False
        return True

def isAlienSorted_naive(words, order):
    d = {}
    for k, v in enumerate(order):
        d[v] = k
    for w_ix in range(len(words) - 1):
        for l_ix in range(min(len(words[w_ix]), len(words[w_ix + 1]))):
            if d[words[w_ix][l_ix]] > d[words[w_ix + 1][l_ix]]:
                return False
            # elif d[words[w_ix][l_ix]] < d[words[w_ix + 1][l_ix]]:
            #     return True
            else:
                continue
    return True if len(words[w_ix]) < len(words[w_ix + 1]) else False


def isAlienSorted_lambda(words, order):
    return words == sorted(words, key = lambda x: [order.index(c) for c in x])

if __name__ == '__main__':
    print(isAlienSorted(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
    print(isAlienSorted(["word", "world", "row"], 'worldabcefghijkmnpqstuvxyz'))
    print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
    print(isAlienSorted(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
    print(isAlienSorted_naive(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
    print(isAlienSorted_naive(["word", "world", "row"], 'worldabcefghijkmnpqstuvxyz'))
    print(isAlienSorted_naive(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
    print(isAlienSorted_naive(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
    print(isAlienSorted_lambda(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
    print(isAlienSorted_lambda(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
    print(isAlienSorted_lambda(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))