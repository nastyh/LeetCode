def addUpTo(nums, k):
    res = []
    for ix, num in enumerate(nums):
        if (k - num) in nums[:ix] + nums[ix+1:]:
            res.append(num)
    return res

if __name__ == '__main__':
    print(addUpTo([3,7, -1, 14, 9], 6))
