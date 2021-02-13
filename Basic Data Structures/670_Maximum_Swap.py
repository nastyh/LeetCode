def maximumSwap(num):  # brute force  O(n*2) and O(n)
    """
    Convert integer into list of digits and create a current_max variable as a sort of checkpoint.
    For each digit in num, swap that digit with every succeeding digit.
    Compare the current swapped number with the current maximum value and swap if it's greater.
    Make sure you undo the swap you did, since we're only allowed to swap once.
    Return the final value as an integer format.
    """
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


def maximumSwap_dict(num):  # O(n) both 
    """
    compute last[d] = i, the index i of the last occurrence of digit d (if it exists).
    when scanning the number from left to right, if there is a larger digit in the future,
    we will swap it with the largest such digit; if there are multiple such digits,
    we will swap it with the one that occurs the latest.
    """
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