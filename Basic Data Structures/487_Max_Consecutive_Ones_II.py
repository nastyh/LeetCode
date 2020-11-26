import math
def findMaxConsecutiveOnes(nums):
    l, r = 0, 0
    max_zeroes = 1

    while r < len(nums):
        if nums[r] == 0:
            max_zeroes -= 1
        if max_zeroes < 0:
            if nums[l] == 0:
                max_zeroes += 1
                l += 1
            else:
                l += 1
        r += 1
    return r - l
    

def findMaxConsecutiveOnes_alt(nums):
    res = 0
    l, t, num_of_zeros = 0, 1, 0
    for r in range(len(nums)):
        if nums[r] == 0:
            num_of_zeros += 1
        while num_of_zeros > t:
            if nums[l] == 0:
                num_of_zeros -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

if __name__ == '__main__':
    print(findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
    print(findMaxConsecutiveOnes([1, 1, 0, 1]))
    print(findMaxConsecutiveOnes_alt([1, 0, 1, 1, 0]))
    print(findMaxConsecutiveOnes_alt([1, 1, 0, 1]))
    print(findMaxConsecutiveOnes_alt([1, 1, 1, 0, 0, 1, 1, 1, 1]))

