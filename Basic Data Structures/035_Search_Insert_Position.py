def searchInsert(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (r - l) // 2 + l
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m
        else:
            l = m + 1
    return l


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 5))
    print(searchInsert([1, 3, 5, 6], 2))
    print(searchInsert([1, 3, 5, 6], 7))
    print(searchInsert([1, 3, 5, 6], 0))