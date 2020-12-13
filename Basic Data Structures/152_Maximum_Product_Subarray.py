import math
def maxProduct(nums):
    maxval = float('-inf')
    imax, imin= 1, 1
    for i in range(len(nums)):
        if nums[i] < 0:
            imax, imin = imin, imax
        imax = max(imax * nums[i], nums[i])
        imin = min(imin * nums[i], nums[i])
        maxval = max(maxval, imax)
    return maxval


def maxProduct_Kadane(nums):
    dp = [None] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] * dp[i - 1])
    return max(dp)


def maxProduct_reversal(nums):  # O(2n) and O(1)
    nums_rev = nums[::-1]
    for i in range(1, len(nums)):
        if nums[i - 1] != 0:    # creating a running multiplication. If there is a zero, skip it
            nums[i] *= nums[i - 1]
        if nums_rev[i - 1] != 0:  # creating a running multiplication. If there is a zero, skip it
            nums_rev[i] *= nums_rev[i - 1]
    return max(max(nums), max(nums_rev))  # return the abs max


def maxProduct_alt(nums):
    if not nums: return 0
    cur_max = final_max = cur_min = nums[0]
    for i in range(1, len(nums)):
        temp = cur_max
        cur_max = max(max(cur_max * nums[i], cur_min * nums[i]), nums[i])
        cur_min = min(min(temp * nums[i] , cur_min * nums[i]), nums[i])
        if cur_max > final_max:
            final_max = cur_max
    return final_max
    

def maxProduct_brute_force(nums):  # O(n^2)
        res, curr = -math.inf, 1
        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i + 1, len(nums)):
                curr = curr * nums[j]
                res = max(res, curr)
        return res


def maxProduct_brute_force_another(nums):  # O(n^2)
    res, curr = -math.inf, 1
    for l in range(len(nums) - 1):
        for r in range(len(nums)):
            curr *= nums[r]
            res = max(res, curr)
        curr = 1
    return res


if __name__ == '__main__':
    print(maxProduct([2, 3, -2, 4]))
    print(maxProduct_alt([2, 3, -2, 4]))
    print(maxProduct_brute_force([2, 3, -2, 4]))
    print(maxProduct([-2, 0, -1]))
    print(maxProduct_alt([-2, 0, -1]))
    print(maxProduct_brute_force([-2, 0, -1]))
    print(maxProduct([-4, -3, -2]))
    print(maxProduct_alt([-4, -3, -2]))
    print(maxProduct_brute_force([-4, -3, -2]))
    print(maxProduct([-2, 3, -4]))
    print(maxProduct_alt([-2, 3, -4]))
    print(maxProduct_brute_force([-2, 3, -4]))
    print(maxProduct_brute_force_another([-2, 3, -4]))
    print(maxProduct_brute_force_another([2, 3, -2, 4]))
    print(maxProduct_brute_force_another([-2, 0, -1]))
