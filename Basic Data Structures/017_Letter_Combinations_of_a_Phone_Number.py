from itertools import product
from collections import Counter

def letterCombinations_recur(digits):
    """
    Recursive approach
    First, write down a condition when curr_res should be appended to res
    Second, the main part starts
    We need to take every digit in digits, and every letter associated with this digits in the dictionary
    """
    d = {"2" : ["a" , "b" , "c"],
            "3" : ["d" , "e" , "f"],
            "4" : ["g" , "h" , "i"],
            "5" : ["j" , "k" , "l"],
            "6" : ["m" , "n" , "o"],
            "7" : ["p" , "q" , "r" , "s"],
            "8" : ["t" , "u" , "v"],
            "9" : ["w" , "x" , "y" , "z"]}
    res = []
    if len(digits) == 0: return res
    def _recur(digits, d, curr_res, curr_ix):
        if len(curr_res) == len(digits):
            res.append(curr_res)
            return
        for i in range(curr_ix, len(digits)):
            for ch in d[digits[i]]:
                _recur(digits, d, curr_res + ch, i + 1)  # need to do curr_res + ch inside _recur. If you do outside, won't work
    _recur(digits, d, '', 0)
    return res


def letterCombinations(digits):
    res, l = '', []
    d = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'
         }
    possible = [d[x] for x in digits]
    return [''.join(x) for x in product(*possible) if x]
    

def letterCombinations_alt(digits):
    def findCombination(currentComb , digit):
        if not digit:
            result.append(currentComb)
        else:
            for i in phoneDic[digit[0]]:
                findCombination(currentComb + i , digit[1 : ])
    result = []
    phoneDic = {"2" : ["a" , "b" , "c"],
                "3" : ["d" , "e" , "f"],
                "4" : ["g" , "h" , "i"],
                "5" : ["j" , "k" , "l"],
                "6" : ["m" , "n" , "o"],
                "7" : ["p" , "q" , "r" , "s"],
                "8" : ["t" , "u" , "v"],
                "9" : ["w" , "x" , "y" , "z"]}
    if digits:
        findCombination("" , digits)
    return result


def letterCombinations_iter(digits):
    if len(digits) == 0: return []
    if len(digits) == 1: return [i for i in digits]
    d = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    res = [""]
    for digit in digits:
        curr_res = []
        for val in res:
            for ch in d[digit]:
                curr_res.append(val + ch)
        res = curr_res
    return res
        

def letterCombinations_another(digits):  # O(3^N * 4^M) both, where N is the number of digits in the input that maps to 3 letters, and M -- maps to 4 letters
    """
    This is backtracking b/c we remove an element from curr
    """
    d = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'
         }
    if len(digits) == 0: return []
    def _helper(digits, d, ix, curr, res):
        if ix == len(digits):
            res.append(curr)
            return
        for ch in d[digits[ix]]:
            curr += ch
            _helper(digits, d, ix + 1, curr, res)
            curr = curr[:-1]
        return res
    return _helper(digits, d, 0, '', [])


def letterCombinations_one_more(digits):
    d = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'
         }
    res = []
    if len(digits) == 0: return []
    if len(digits) == 1: return [digits[0]]
    def _helper(digits, d, curr_ix, curr_res):
        if len(curr_res) == len(digits):
            res.append(curr_res)
            return
        for i in range(curr_ix, len(digits)):
            for ch in d[digits[i]]:
                curr_res += ch
                _helper(digits, d, i + 1, curr_res)
                curr_res = curr_res[:-1]
    _helper(digits, d, 0, '')
    return res


if __name__ == '__main__':
    # print(letterCombinations('23'))
    # print(letterCombinations_alt('23'))
    # print(letterCombinations_iter('23'))
    # print(letterCombinations_another('23'))
    print(letterCombinations_one_more('23'))
    print(letterCombinations_one_more('2'))
