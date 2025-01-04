"""
Given an array of integers and integer A, find the integer in the array that is closest to A
"""
def find_closest(nums, target):
    """
    O(n) and O(1)
    just go over, calculate the diff, compare w/
    what we've seen already, if it's better, update res 
    """
    res, glob_diff = -1, math.inf
    for num in nums:
        if abs(num - target) < glob_diff:
            glob_diff = abs(num - target)
            res = num 
    return res