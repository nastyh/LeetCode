import math
def minOperations(nums):  # O(n) and O(1)
    """
    Step 1: Calculate the total sum of nums.
    Step 2: Initialize two pointers left and right to 0. Initialize an integer current to represent the sum from nums[0] to nums[left-1] and
    from nums[right+1] to nums[last]. Initialize an integer mini to record the minimum length that sums up to x
    Step 3: Iterate right form 0 to the end of nums. In each iteration:
    Update current.
    If current is smaller than x, move left to left.
    If current is equal to x, update the maximum length.
    Step 4: Return the result.
    """
    current = sum(nums)
    n = len(nums)
    mini = math.inf
    left = 0
    for right in range(n):
        # sum([0,..,left) + (right,...,n-1]) = x
        current -= nums[right]
        # if smaller, move `left` to left
        while current < x and left <= right:
            current += nums[left]
            left += 1
        # check if equal
        if current == x:
            mini = min(mini, (n - 1- right) + left)
    return mini if mini != inf else -1


def minOperations_alt(nums):  # O(n) and O(1)
    """
    Step 1: Calculate the total sum of nums. Mark as total.
    Step 2: Initialize two pointers left and right to 0. Initialize an integer current to represent the sum from nums[left] to nums[right], inclusively.
    Initialize an integer maxi to record the maximum length that sums up to total - x.
    Step 3: Iterate right form 0 to the end of nums. In each iteration:
    Update current.
    If current is greater than total - x, move left to left.
    If current is equal to total - x, update the maximum length.
    Step 4: Return the result.
    """
    total = sum(nums)
    n = len(nums)
    maxi = -1
    left = 0
    current = 0
    for right in range(n):
        # sum([left ,..., right]) = total - x
        current += nums[right]
        # if larger, move `left` to left
        while current > total - x and left <= right:
            current -= nums[left]
            left += 1
        # check if equal
        if current == total-x:
            maxi = max(maxi, right - left + 1)
    return n - maxi if maxi != -1 else -1