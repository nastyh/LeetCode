def singleNonDuplicate(nums):  # O(logn) and O(1)
    """
    search on even indices only
    The last index of an odd-lengthed array is always even, so we can set lo and hi to be the start and end of the array.
    make sure our mid index is even. We can do this by dividing lo and hi in the usual way, but then decrementing it by 1 if it is odd.
    This also ensures that if we have an even number of even indexes to search, that we are getting the lower middle 
    Then we check whether or not the mid index is the same as the one after it.
    If it is, then we know that mid is not the single element, and that the single element must be at an even index after mid.
    Therefore, we set lo to be mid + 2. It is +2 rather than the usual +1 because we want it to point at an even index.
    If it is not, then we know that the single element is either at mid, or at some index before mid. Therefore, we set hi to be mid.
    """
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if m % 2 == 0:
            if nums[m] == nums[m - 1]:
                r = m - 2
            elif nums[m] == nums[m + 1]:
                l = m + 2
            else:
                return nums[m]
        else:
            if nums[m] == nums[m - 1]:
                l = m + 1
            else:
                r = m - 1 
    return nums[l]


def singleNonDuplicate_alt(nums):
    """
    Do edge checks first
    Idea is that pairs always start at an even index and end at an odd index
    """
    if len(nums) == 1:
        return nums[0]
    l, r = 0, len(nums) - 1
    if nums[l] != nums[l + 1]:
        return nums[l]
    if nums[r] != nums[r - 1]:
        return nums[r]
    while l < r:
        m = l + (r - l) // 2
        if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
            return nums[m]
        if nums[m] == nums[m - 1]:
            if m % 2 == 1:  # means we're looking at the second element of the pair and its index is odd. 
                l = m + 1  # answer should be to the right, b/c to the left all pairs are good based on the definition of well-formed pairs
            else:
                r = m - 1  # pairs to the left are not well-formed, thus, look in the left part
        if nums[m] == nums[m + 1]:
            if m % 2 == 1:  # means that a pair starts at an odd index, it's against the definition of a well-formed pair
                r = m - 1  # go to the left, b/c this is where something is wrong
            else:
                l = m + 1  # go to the right b/c everything to the right is good 
    return nums[l]






def singleNonDuplicate_xor(nums):  # O(N) and O(1)
    """
    0 ^ number is number
    number ^ number is 0
    Eventually we end with a situation 0 ^ non-repeating element and get this non-repeating element
    """
    res = 0
    for num in nums:
        res ^= num
    return res


if __name__ == '__main__':
    print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
    print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
