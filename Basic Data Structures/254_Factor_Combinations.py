def getFactors(n):
    if n < 4: return []
    res = []
    def backtracking(first, path, target):
        for num in range(first, target):
            if num * num > target:
                return 
            if target % num == 0:
                res.append(path + [num, target//num])
                backtracking(num, path + [num], target//num)
    backtracking(2, [], n)
    return res


def getFactors_iter(n):
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


if __name__ == '__main__':
    print(getFactors(12))
    print(getFactors_iter(12))