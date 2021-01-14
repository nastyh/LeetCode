import math
"""
Given an array, print a smallest sum of two non-adjacent elements
[1, 2, 5, 6, 3] -> 4 (you can't pick 1 & 2 because they are next to each other)
[2, 0, 2, 3] -> 3
"""

def smallest_sum(nums):  # O(n) and O(1)
    """
    Optimal solution
    Start with smallest_non_last, which is the min of the first two elements 
    Loop starts with the third element
    We might update smallest_non_last if it's better than what we've already seen. 
    Smallest_sum it's either taking the current element and the best values of smallest_non_last or taking 
    a sum of the previous element and the element three elements to the left
    """
    if len(nums) < 3: return None
    smallest_sum = math.inf
    smallest_non_last = min(nums[0], nums[1])  # min of two first elements
    for i in range(2, len(nums)):
        smallest_non_last = min(smallest_non_last, min(nums[i - 3], nums[i - 2]))
        smallest_sum = min(nums[i] + smallest_non_last, nums[i - 1] + nums[i - 3])
    return smallest_sum


def smallest_sum_dp(nums):  # O(n) both
    """
    Need two extra lists:
    dp is where the answer will be 
    smallest is the list where, staring from the third index, we keep the smallest element from nums that 
    stands to the left from the i-1 element
    In dp, the first two elements are equal to respective from nums
    Third is the sum of the previous two
    After that we start the loop and choose the min 
    """
    if len(nums) < 3: return None
    dp = [None] * len(nums)
    smallest = [math.inf] * len(nums)
    for i in range(2, len(nums)):
        smallest[i] = min(nums[:i - 1])

    # alternative way to do smallest, b/c the above might be not linear
    # smallest[0], smallest[1] = nums[0], nums[1]
    # for i in range(2, len(nums)):
    #     smallest[i] = min(smallest[i - 2], smallest[i - 1])
    # end of the alternative way 

    dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[1]
    for i in range(3, len(nums)):
        dp[i] = min(nums[i] + smallest[i], nums[i - 1] + nums[i - 1])
    return dp[-1]


if __name__ == '__main__':
    print(smallest_sum([1, 2, 5, 6, 3]))
    print(smallest_sum([2, 0, 2, 3]))
    print(smallest_sum([4, 4, 4]))
    print(smallest_sum_dp([1, 2, 5, 6, 3]))
    print(smallest_sum_dp([2, 0, 2, 3]))
    print(smallest_sum_dp([4, 4, 4]))
