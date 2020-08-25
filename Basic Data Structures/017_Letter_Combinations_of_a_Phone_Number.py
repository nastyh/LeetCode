from itertools import product
from collections import Counter
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


def letterCombinations_another(digits):
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
    if len(digits) == 1: return [digits[0]]
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


if __name__ == '__main__':
    print(letterCombinations('23'))
    print(letterCombinations_alt('23'))
    print(letterCombinations_another('23'))
