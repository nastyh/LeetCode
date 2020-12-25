def removeElement(nums, val)
    res = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[res], nums[i] = nums[i], nums[res]
            res += 1
    return res
