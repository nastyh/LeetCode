import math
def findMaxConsecutiveOnes(nums):
    l, r = 0, 0
    curr, glob = 0, -math.inf
    max_zeroes = 1

    while r < len(nums):
        if nums[r] == 0:
            max_zeroes -= 1
        curr = r - l
        glob = max(glob, curr)
        if max_zeroes < 0:
            if nums[l] == 0:
                max_zeroes += 1
                l += 1
            else:
                l += 1
        r += 1
    return r - l

if __name__ == '__main__':
    print(findMaxConsecutiveOnes([1,0,1,1,0]))
    print(findMaxConsecutiveOnes([1,1,0,1]))
