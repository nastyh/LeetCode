def findMaxAverage(nums, k):
    if len(nums) <= k: return sum(nums) / k
    curr_res, glob_res = sum(nums[:k]), sum(nums[:k])
    l = 0
    for r in range(k, len(nums)):
        curr_res = curr_res - nums[l] + nums[r]
        glob_res = max(glob_res, curr_res)
        l += 1
    return glob_res / k

def findMaxAverage_alt(nums, k):
    """
    Start with the array of length k in the beginning
    Then start moving the pointer i (it's the right pointer, we can save on creating the left pointer b/c we can do i - k + 1)
    Subtract the value at the left pointer
    Increment the right pointer
    Add the value at the new right pointer 
    """
    if len(nums) == 1: return max(nums)
    if len(nums) == k: return sum(nums) / k
    i = k - 1 
    curr_sum = sum(nums[:i + 1])
    glob_res = curr_sum
    while i < len(nums) - 1:
        curr_sum -= nums[i - k + 1]
        i += 1
        curr_sum += nums[i]
        glob_res = max(glob_res, curr_sum)
    return glob_res / k


if __name__ == '__main__':
    print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(findMaxAverage_alt([1, 12, -5, -6, 50, 3], 4))