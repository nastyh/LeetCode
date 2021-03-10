import math
def getFactors(n):
    if n < 4: return []
    res = []
    def backtracking(first, path, target):
        for num in range(first, target):
            if num * num > target:
                return 
            if target % num == 0:
                res.append(path + [num, target // num])
                backtracking(num, path + [num], target // num)
    backtracking(2, [], n)
    return res


def getFactors_another(n):
    """
    First, an edge case
    Then in helper we do a loop.
    Potential candidates are numbers from 2 to sqrt(n) + 1.
    If n can be divided by the current number, it's good: add to the res what we already have plus both numbrers
    Otherwise, call the function again by make n lower
    """
    if n < 4: return []
    res = []
    def _helper(st_num, curr_res, n):
        for i in range(st_num, int(math.sqrt(n)) + 1):
            if i * i > n:
                return
            if n % i == 0:
                res.append(curr_res + [i, n // i]))
                _helper(i, curr_res + [i], n // i)      
    _helper(2, [], n)
    return res


def getFactors_iter(n):  # O(n) both
    ans, stack, x = [], [], 2
    while True:
        if x > n / x:
            if not stack:
                return ans
            ans.append(stack + [n])
            x = stack.pop()
            n *= x
            x += 1
        elif n % x == 0:
            stack.append(int(x))
            n //= x
        else:
            x += 1
    return ans



if __name__ == '__main__':
    # print(getFactors(12))
    print(getFactors_iter(12))