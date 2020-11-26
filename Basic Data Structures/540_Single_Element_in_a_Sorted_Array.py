def singleNonDuplicate(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if m % 2 == 0:
            if nums[m] == nums[m - 1]:
                r = m - 2
            elif nums[m] == nums[m + 1]:
                l = m + 2
            else:
                return nums[m]
        else:
            if nums[m] == nums[m - 1]:
                l = m + 1
            else:
                r = m - 1 
    return nums[l]


if __name__ == '__main__':
    print(singleNonDuplicate([1, 1, 2, 3, 3 ,4, 4, 8, 8]))
    print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
