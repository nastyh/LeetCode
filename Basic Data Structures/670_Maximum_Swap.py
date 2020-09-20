def maximumSwap(num):  # brute force
    digits = list(map(str, list(str(num))))
    current_max = digits.copy()
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            digits[i], digits[j] = digits[j], digits[i]              
            if int(''.join(list(map(str, digits)))) > int(''.join(list(map(str, current_max)))):
                current_max = digits.copy()                 
            digits[i], digits[j] = digits[j], digits[i]
    return int(''.join(list(map(str, current_max))))


def maximumSwap_greedy(num):
    num = [int(i) for i in str(num)]
    for i in range(len(num)-1):
        m = max(num[i + 1:])
        if num[i] < m:
            for j in range(len(num) - 1, i, -1):
                if num[j] == m:
                    break
            num[i], num[j] = num[j], num[i]
            break
    return int("".join([str(i) for i in num]))


def maximumSwap_dict(num):
    nums = [int(i) for i in str(num)]
    d = {}
    for k, v in enumerate(nums):
        d[v] = k
    for k, v in enumerate(nums):
        for n in range(9, v, -1):
            if n in d and d[n] > k:
                nums[k], nums[d[n]] = nums[d[n]], nums[k]
                return int("".join([str(i) for i in nums]))
    return num
                


if __name__ == '__main__':
    print(maximumSwap(98368))
    print(maximumSwap_greedy(98368))
    print(maximumSwap_dict(98368))