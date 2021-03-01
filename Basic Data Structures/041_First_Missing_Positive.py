def firstMissingPositive(nums):  # O(n) and O(1)
    """
    have an array with n cells (n is the length of the array). If an integer is missing it must be in the range [1..n]
    two possibilities:

    there is no missing integer in the array
    there is a missing integer in the array.
    If there is no missing integer, this means that the array has all number from 1 to n.
    This must mean that the array is full. Why, because in the range [1..n] there are exactly n numbers, and if you place n numbers in an array of length n,
    the array is by definition full. (in this case solution is to return n+1 which is the first smallest integer).
     If there is a missing integer (or more than one), the missing integer(s), let's call it X, must be in the range 1..n.
     Why, because if the missing integer X is not in the range [1..n] that would imply that all integers [1..n] are in the array,
     which would mean that the array is full, leaving no space where to place X (since X is not in the range [1..n]).
    """
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums): nums[i] = len(nums) + 1
    
    # use abs() to avoid index out of range
    for a in nums:
        a = abs(a)
        if a <= len(nums) and nums[a - 1]>=0: nums[a - 1] *= -1
    
    for i, a in enumerate(nums):
        if a > 0: return i + 1
    return len(nums) + 1


def firstMissingPositive_dict(nums):  # O(n) both
    d = {num : 1 for num in nums}
    res = 1
    while True:
        try:
            d[res]
        except:
            return res
        res += 1