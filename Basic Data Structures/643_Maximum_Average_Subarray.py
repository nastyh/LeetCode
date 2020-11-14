def findMaxAverage(nums, k):
    if len(nums) <= k: return sum(nums) / k
    curr_res, glob_res = sum(nums[:k]), sum(nums[:k])
    l = 0
    for r in range(k, len(nums)):
        curr_res = curr_res - nums[l] + nums[r]
        glob_res = max(glob_res, curr_res)
        l += 1
    return glob_res / k


if __name__ == '__main__':
    print(findMaxAverage([1,12,-5,-6,50,3], 4))