def permute(nums):
    if len(nums) == 1: return [nums]
    res = []

    perms = permute(nums[1:])
    first = nums[0]
    level = []
    for perm in perms:
        for i in range(len(perm) + 1):
            level.append(perm[:i] + first + perm[i:])
        res.append(level)
    return level

if __name__ == '__main__':
    print(permute('123'))
