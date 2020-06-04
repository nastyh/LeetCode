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
        res = []
        d = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'
         }

        return _helper(result, digits, "", 0, d)







    # for digit in digits:
    #     res += ''.join(d[int(digit)])
    # # return d[int(digits)]
    # # res += ''.join([v for k, v in d.items()])
    # l = [i for i in product(res, repeat = len(digits))]
    # return l


if __name__ == '__main__':
    print(letterCombinations('23'))
