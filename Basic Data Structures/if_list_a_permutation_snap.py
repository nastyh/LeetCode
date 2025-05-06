"""
Checks if a given list of numbers is a permutation.
A list nums (with length n) should contain every integer from 1 to n exactly once.
"""
def is_permutation_expected(nums):
    """
    O(N)
    O(1)
    The numbers themselves tell us where they belong (value v should be at index v − 1).
    We repeatedly swap each out‑of‑place element into its target slot.

    If we ever meet
    1. a value that is out of the range [1, n], or
    2. a duplicate already sitting in its correct slot,
    then the list cannot be a permutation.

    Because every swap puts at least one value into its final position,
    the total number of swaps is ≤ n, so the overall complexity is linear.
    All work is done in the original array,
    """
    n = len(nums)
    i = 0
    while i < n:
        v = nums[i]

        # value must be in 1..n
        if v < 1 or v > n:
            return False
        correct = v - 1
        if nums[correct] == v:
            # already positioned
            if i == correct:
                i += 1
            else:           # duplicate encountered
                return False
        else:
            # place v where it belongs
            nums[i], nums[correct] = nums[correct], nums[i]
    return True
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
