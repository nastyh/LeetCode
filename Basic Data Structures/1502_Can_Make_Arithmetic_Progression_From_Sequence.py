def canMakeArithmeticProgression(arr):  # brute force
    res = []
    arr.sort()
    for i in range(len(arr) - 1):
        res.append(arr[i + 1]  - arr[i])
    return len(set(res)) == 1
    

def canMakeArithmeticProgression_alt(arr):  # also brute force but without an extra list
    if len(arr) < 2: return True
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != diff:
            return False
    return True


def canMakeArithmeticProgression_math(arr):
    d = (max(arr) - min(arr)) / (len(arr) - 1)
    return d


if __name__ == '__main__':
    print(canMakeArithmeticProgression_alt([3, 5, 1]))
    print(canMakeArithmeticProgression_math([3, 5, 1]))
