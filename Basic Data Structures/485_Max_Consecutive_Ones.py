def findMaxConsecutiveOnes(nums):
    glob_res, curr_res = 0, 0
    if len(nums) == 1:
        if nums[0] == 1:
            return 1
        else:
            return 0
    for i in range(len(nums)):
        if nums[i] == 1:
            curr_res += 1
            glob_res = max(glob_res, curr_res)
        else:
            curr_res = 0
    return glob_res


if __name__ == '__main__':
    print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))