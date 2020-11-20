def search(nums, target):  # DOESN'T WORK FOR EDGE CASES
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    def _unpivot(nums):
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                pivot_ix = i
                nums_upd = nums[pivot_ix + 1:] + nums[:pivot_ix + 1]
                break
            else:
                pivot_ix = 0
                nums_upd = nums
        return nums_upd, pivot_ix
    def _binsearch(arr, target, pivot_ix):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                if pivot_ix != 0:
                    return abs(m - pivot_ix) + 1
                else:
                    return m
            elif arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                r = m - 1
        return -1
    nums_upd, pivot_ix = _unpivot(nums)
    # return nums_upd
    return _binsearch(nums_upd, target, pivot_ix)


def search_working(nums, target):
    def _findpivot(arr):
        pivot_ix = None
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                pivot_ix = i
                break
        return pivot_ix
    def _binsearch(arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m] == target:
                return m
            elif arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                r = m - 1
        return -1
    pivot_ix = _findpivot(nums)
    return _binsearch(nums[:pivot_ix + 1], target) + pivot_ix + 1
    # return pivot_ix
    if pivot_ix is None:
        return _binsearch(nums, target)
    # return _binsearch(nums[pivot_ix + 1:], target) + pivot_ix + 1 if _binsearch(nums[pivot_ix + 1:], target) != -1 else -1
    if nums[0] > target:
        return _binsearch(nums[pivot_ix + 1:], target) + pivot_ix + 1 if _binsearch(nums[pivot_ix + 1:], target) != -1 else -1
    elif nums[0] < target:
        return _binsearch(nums[:pivot_ix + 1], target) + pivot_ix + 1 if _binsearch(nums[pivot_ix + 1:], target) != -1 else -1
    else:
        return 0


def _test_binsearch(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
    return -1


if __name__ == '__main__':
    # print(search([4, 5, 6, 7, 0, 1, 2], 0))
    # print(search([1, 3], 1))
    # print(search_working([4, 5, 6, 7, 0, 1, 2], 0))
    # print(search_working([1, 3], 1))
    # print(search_working([3, 1], 1))
    # print(search_working([4, 5, 6, 7, 0, 1, 2], 3))
    # print(search_working([3, 5, 1], 3))
    print(search_working([3, 5, 1], 5))
    # print(_test_binsearch([1], 1))
