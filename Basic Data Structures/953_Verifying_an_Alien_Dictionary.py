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


def isAlienSorted_sorting(words, order):
    """
    The most annoying but possible to come up with
    Edge case: one word in words. Make sure that it is == to itself sorted by order
    Then we build a list of lists 'orders.' Every element contains indices of characters of respective words
    Then we start comparing first to second, second to third, all the way to the end
    Then we have the main if statement
    If the index of the character from the left word is larger than that from the right word, it's bad, return False immediately
    If the index of the character from the left word is smaller than that from the left word, it's good, don't need to check this pair of words anymore
    If the indices are equal, keep looking for differences
    We need to wrap this if statement in a "try" statement, to handle ['apple', 'app'] cases, i.e. when the left word is longer and we are about to get the IndexError. 
    If we iterate through the "app" parts of the both words and nothing yet happened, but the longer word goes before the shorter word, it's bad, thus, return False 
    """ 
    if len(words) == 1:
        if words[0] == sorted(words[0], key = order): return True
        else: return False
    orders = []
    for word in words:
        curr_indices = []
        for ch in word:
            curr_indices.append(order.index(ch))
        orders.append(curr_indices)
    for ix in range(len(orders) - 1):
        try:
            for ch_ix in range(len(orders[ix])):
                if orders[ix][ch_ix] > orders[ix + 1][ch_ix]:
                    return False
                elif orders[ix][ch_ix] < orders[ix + 1][ch_ix]:
                    break
                else: continue
        except IndexError:
            return False
    return True



if __name__ == '__main__':
    # print(isAlienSorted(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
    # print(isAlienSorted(["word", "world", "row"], 'worldabcefghijkmnpqstuvxyz'))
    # print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
    # print(isAlienSorted(["hello","hello"], "abcdefghijklmnopqrstuvwxyz"))
    # print(isAlienSorted(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
    # print(isAlienSorted_naive(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
    # print(isAlienSorted_naive(["word", "world", "row"], 'worldabcefghijkmnpqstuvxyz'))
    # print(isAlienSorted_naive(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
    # print(isAlienSorted_naive(["hello","hello"], "abcdefghijklmnopqrstuvwxyz"))
    # print(isAlienSorted_naive(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
    # print(isAlienSorted_lambda(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
    # print(isAlienSorted_lambda(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
    # print(isAlienSorted_lambda(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
    print(isAlienSorted_sorting(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz'))
    print(isAlienSorted_sorting(["word", "world", "row"], 'worldabcefghijkmnpqstuvxyz'))
    print(isAlienSorted_sorting(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
    print(isAlienSorted_sorting(["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"], "zkgwaverfimqxbnctdplsjyohu"))
    print(isAlienSorted_sorting(["hello", "hello"], "abcdefghijklmnopqrstuvwxyz"))