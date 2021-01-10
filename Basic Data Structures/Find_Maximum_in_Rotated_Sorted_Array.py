def findMax(nums):
    """
    the edge case is important, b/c it's impossible to have 
    [5, .... some max number .... then some small numbers ... another number that is > 5]
    """
    if len(nums) == 0: return -1
    if len(nums) == 1: return nums[0]
    if nums[0] < nums[-1]: return nums[-1]  # edge case: already sorted array
    l, r = 0, len(nums) - 1
    res = -1
    while l < r:
        m = l + (r - l) // 2
        if m == 0 or nums[m] > nums[m - 1]:  # avoiding IndexError
            res = nums[m]
            l = m + 1  # we still might find a larger number to the right
        elif nums[m] <= nums[m - 1]:  # we're in the decreasing sequence 
            r = m - 1  
    return res 


if __name__ == '__main__':
    print(findMax([5, 7, 11, 1, 3]))
    print(findMax([7, 9, 15, 1, 3]))
    print(findMax([1, 2]))
    print(findMax([1, 2, 3]))
