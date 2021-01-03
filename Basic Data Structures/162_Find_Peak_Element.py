def findPeakElement(nums):  # O(n) and O(1)
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return i
    return len(nums) - 1


def findPeakElement_linear(nums):
    """
    Two edge cases
    If it's a decresing array, return 0
    If it's an increasing array, return len(nums) - 1
    otherwise compare elements in triples
    At the end return len(nums) - 1 to account for cases like "[3, 1, 2]"
    """
    if len(nums) == 1: return 0
    if len(nums) == 2:
        return nums.index(max(nums))
    if all(nums[i + 1] < nums[i] for i in range(len(nums) - 1)):
        return 0
    if all(nums[i + 1] > nums[i] for i in range(len(nums) - 1)):
        return len(nums) - 1
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i
    return len(nums) - 1


def findPeakElement_bin_search_recursive(nums):  # O(logn) and O(logn)
    def _helper(arr, l, r):
        if l == r:
            return l
        m = l + (r - l) // 2
        if arr[m] > arr[m + 1]:
            return _helper(arr, l, m)
        else:
            return _helper(arr, m + 1, r)
    return _helper(nums, 0, len(nums) - 1)


def findPeakElement_bin_search_iter(nums):  # O(logn) and O(logn)
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] > nums[m + 1]:
            r = m
        else:
            l = m + 1
    return l 