def threeSum(nums):
    res, curr = [], []
    for i, num in enumerate(nums):
        for j, internal in enumerate(nums[:i] + nums[i+1:]):
            if 0 - internal in nums[:j] + nums[j+1:]:
                curr.append(internal)
        res.append(curr)
    return res

if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))
