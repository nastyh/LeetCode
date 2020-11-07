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


def isMajorityElement_alt(nums, target):
    """
    In a sorted array the majority element has to be at location n // 2 or n // 2 + 1 depending
    on whether the length of nums is even or odd
    """
    return nums[len(nums) // 2] == target



if __name__ == '__main__':
    print(isMajorityElement([2, 4, 5, 5, 5, 5, 5, 6, 6], 5))
    print(isMajorityElement([10, 100, 101, 101], 101))

