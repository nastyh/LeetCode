"""
Checks if a given list of numbers is a permutation.
"""
def is_permutation(nums):
    """
    O(n)
    O(1)
    """
    if len(set(nums)) != len(nums): # all elements should be unique
        return False

    # Check if the list contains all numbers from 1 to n
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return actual_sum == expected_sum

def is_permutation_another(nums):
    """
    O(n) both 
    """
    n = len(nums)
    seen = [False] * (n + 1)      # we'll ignore index 0
    for x in nums:
        # if x is out of range or already seen, it can't be a permutation
        if x < 1 or x > n or seen[x]:
            return False
        seen[x] = True
    # if we never returned False, all numbers 1..n appeared exactly once
    return True
