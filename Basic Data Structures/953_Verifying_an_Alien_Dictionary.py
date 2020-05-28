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

if __name__ == '__main__':
    print(isAlienSorted(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
    print(isAlienSorted(["word", "world", "row"], 'worldabcefghijkmnpqstuvxyz'))
    print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))

