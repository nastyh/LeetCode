def findDuplicates(nums):
    res = []
    for i in nums:
        if nums[abs(i) - 1] >= 0:
            nums[abs(i) - 1] *= -1
        else:
            res.append(nums[abs(i) - 1])
    return res 

        