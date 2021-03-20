import math
def maxProduct(nums):
    maxval = float('-inf')
    imax, imin = 1, 1
    for i in range(len(nums)):
        if nums[i] < 0:
            imax, imin = imin, imax
        imax = max(imax * nums[i], nums[i])
        imin = min(imin * nums[i], nums[i])
        maxval = max(maxval, imax)
    return maxval


def maxProduct_reversal(nums):  # O(2n) and O(1)
    nums_rev = nums[::-1]
    for i in range(1, len(nums)):
        if nums[i - 1] != 0:    # creating a running multiplication. If there is a zero, skip it
            nums[i] *= nums[i - 1]
        if nums_rev[i - 1] != 0:  # creating a running multiplication. If there is a zero, skip it
            nums_rev[i] *= nums_rev[i - 1]
    return max(max(nums), max(nums_rev))  # return the abs max


def maxProduct_alt(nums):  # O(n) and O(1)
    if not nums: return 0
    cur_max = final_max = cur_min = nums[0]
    for i in range(1, len(nums)):
        temp = cur_max  # need temp b/c we want the unchanged cur_max in two lines below
        cur_max = max(max(cur_max * nums[i], cur_min * nums[i]), nums[i])
        cur_min = min(min(temp * nums[i] , cur_min * nums[i]), nums[i])
        if cur_max > final_max:
            final_max = cur_max
    return final_max
    

def maxProduct_brute_force(nums):  # O(n^2) and O(1)
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


def maxProduct_find_indices(nums):
    if len(nums) == 0:
        return 0
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far
    end_index = 0
    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

        max_so_far = temp_max
        if max_so_far > result:
            result = max_so_far
            end_index = i  
    cur = nums[end_index]
    j = end_index - 1
    # no change in complexity
    while cur != result and j >= 0:
        cur *= nums[j]
        j -= 1
    print(nums[j + 1:i + 1]) 
    return result


def maxProduct_dp(nums):  # O(n) and O(1)
    """
    curr_min and curr_max are updated every time. Need to account for all possible cases:
    when these variables have positive and negative values and when they're multiplied by positive and negative numbers
    """
    res = max(nums)
    curr_min, curr_max = 1, 1 
    for num in nums:
        if num == 0:
            curr_min, curr_max = 1, 1 
            continue
        tmp = curr_max * num  # need to have tmp b/c otherwise the line for curr_max will mess up the calculations for curr_min
        curr_max = max(num * curr_max, num * curr_min, n)
        curr_min = min(tmp, num * curr_min, n)
        res = max(res, curr_max, curr_min)
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
    print(maxProduct_find_indices([2, 3, -2, 4]))