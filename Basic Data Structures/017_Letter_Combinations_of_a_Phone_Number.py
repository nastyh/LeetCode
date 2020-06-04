from itertools import product
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







    # for digit in digits:
    #     res += ''.join(d[int(digit)])
    # # return d[int(digits)]
    # # res += ''.join([v for k, v in d.items()])
    # l = [i for i in product(res, repeat = len(digits))]
    # return l


if __name__ == '__main__':
    print(letterCombinations('23'))
    print(letterCombinations_alt('23'))
