def wiggleSort(nums):  # O(nlogn) and O(1)
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()
    for i in range(1, len(nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]


def wiggleSort_one_pass(nums):  # O(n) and O(1)
    """
    need to achive:
    nums[even_ix] <= nums[odd_ix] <= nums[even_ix] <= nums[odd_ix] etc
    Swap elements to get there 
    """
    for ix in range(1, len(nums)):
        if ix % 2 == 1 and nums[ix] < nums[ix - 1]:
            nums[ix], nums[ix - 1] = nums[ix - 1], nums[ix]
        if ix % 2 == 0 and nums[ix] > nums[ix - 1]:
            nums[ix], nums[ix - 1] = nums[ix - 1], nums[ix]

