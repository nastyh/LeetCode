def isMajorityElement(nums, target):
    def _getleft(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l
    def _getright(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
    return _getright(nums, target) - _getleft(nums, target) + 1 > len(nums) // 2


def isMajorityElement_another(nums, target): # same as above but without a helper function
    """
    do one pass to find the most left element, save to indices[0]
    do another pass to find the most right element, save to indices[1]
    compare two numbers s
    """
    if len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False
    l, r = 0, len(nums) - 1
    indices = [-1, -1]
    while l < r:
        m = l + (r - l) // 2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    indices[0] = l
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1
    indices[1] = r
    return indices[1] - indices[0] + 1 > len(nums) // 2


def isMajorityElement_one_half(nums, target):
    """
    Same as above but with calculating only the left index.
    Try statement to avoid falling out the bounds 
    """
    if len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False
    l, r = 0, len(nums) - 1
    indices = [-1, -1]
    while l < r:
        m = l + (r - l) // 2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    indices[0] = l
    try:
        return nums[l + len(nums) // 2] == target
    except IndexError:
        return False

def isMajorityElement_alt(nums, target):
    """
    In a sorted array the majority element has to be at location n // 2 or n // 2 + 1 depending
    on whether the length of nums is even or odd
    """
    return nums[len(nums) // 2] == target



if __name__ == '__main__':
    # print(isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5))
    # print(isMajorityElement([10, 100, 101, 101], 101))
    # print(isMajorityElement_another([2, 4, 5, 5, 5, 5, 5, 6, 6], 5))
    # print(isMajorityElement_another([10, 100, 101, 101], 101))
    print(isMajorityElement_one_half([2, 4, 5, 5, 5, 5, 5, 6, 6], 5))
    print(isMajorityElement_one_half([10, 100, 101, 101], 101))

