def fourSum(nums, target):
    res = set()
    nums.sort()
    if (not nums) or nums[0] > 0 or nums[len(nums)-1] < 0:
        return []
    for l in range(len(nums)-3):
        for k in range(l+1, len(nums)-2):
            tar = target-nums[k]-nums[l]
            i = k+1
            j = len(nums)-1
            while(i < j):
                if nums[i]+nums[j] == tar:
                    tmp = (nums[k], nums[i], nums[j], nums[l])
                    res.add(tmp)  # add tuple to set
                    while(i < j and nums[i] == nums[i+1]):
                        i = i+1
                    while(i < j and nums[j] == nums[j-1]):
                        j = j-1
                    i = i+1
                    j = j-1
                elif nums[i]+nums[j] < tar:
                    i = i+1
                else:
                    j = j-1
    return [list(r) for r in res]

if __name__ == '__main__':
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
