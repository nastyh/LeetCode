def deutch_flag(nums):
    l, r, i = 0, len(nums) -1 , 0
    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
            l += 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
    return nums


if __name__ == '__main__':
    print(deutch_flag([1, 0, 2, 1, 0]))
