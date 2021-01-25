def kLengthApart_optimal(nums, k):  # O(n) and O(1)
    """
    Straightforward approach:
    go element by element. If you see a 1, check if the counter is positive (means that there were fewer than k zeroes prior to it).
    Edge case is when we start with 1
    Else, decrement counter b/c you see a zero
    """
    counter = k
    for key, v in enumerate(nums):
        if v == 1:
            if key == 0:
                continue
            else:
                if counter > 0:
                    return False
            counter = k
        else:
            counter -= 1
    return True


def kLengthApart_extra_space(nums, k):  # O(N) both
    """
    collect indices of all zeros in a list.
    Go element by element and compute differences between the elements.
    If this difference <= k, return False. Otherwise, True
    """
    indices = []
    for key, v in enumerate(nums):
        if v == 1:
            indices.append(key)
    for i in range(1, len(indices)):
        if indices[i] - indices[i - 1] <= k:
            return False
    return True


def kLengthApart_bit_manipulation(nums, k):  # O(n) and O(1)
    """
    Convert binary array into integer x
    base cases: return true if x == 0 or k == 0.
    While x is greater than 1:
    Remove trailing 1-bit with the right shift: x >>= 1.
    Remove trailing zeros one by one, and count them using counter count.
    The number of zeros in-between 1-bits should be greater or equal to k.
    Hence, return false if count < k.
    """
    # convert binary array into int
    x = 0
    for num in nums:
        x = (x << 1) | num
    # base case
    if x == 0 or k == 0:
        return True
    # remove trailing zeros
    while x & 1 == 0:
        x = x >> 1
    while x != 1:
        # remove trailing 1-bit
        x = x >> 1
        # count trailing zeros
        count = 0
        while x & 1 == 0:
            x = x >> 1
            count += 1
        # number of zeros in-between 1-bits
        # should be greater than or equal to k
        if count < k:
            return False
    return True
