def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for _ in range(k % len(nums)):
        p = nums.pop()
        nums.insert(0, p)
    return nums

def rotate_alt(nums, k):
    if len(nums) == 0: return []
    if len(nums) == k: return nums
    if k > len(nums):
        rotations = k % len(nums)
    else:
        rotations = k
    # return nums[-rotations:] + nums[:rotations]
    return nums[-rotations:] + nums[:-rotations]


if __name__ == '__main__':
    print(rotate([1,2,3,4,5,6,7], 3))
    print(rotate([-1,-100,3,99], 2))
    print(rotate_alt([1,2,3,4,5,6,7], 3))
    print(rotate_alt([-1,-100,3,99], 2))
