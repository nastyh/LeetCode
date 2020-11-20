def search_one_pass(nums, target):
    begin = 0
    end = len(nums) - 1 
    while begin <= end:
        mid = (begin + end)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[end]: # Left side of mid is sorted
            if  nums[begin] <= target and target < nums[mid]: # Target in the left side
                end = mid - 1
            else: # in right side
                begin = mid + 1
        else: # Right side is sorted
            if  nums[mid] < target and target <= nums[end]: # Target in the right side
                begin = mid + 1
            else: # in left side
                end = mid - 1
    return -1


def search_working(nums, target):  # DOESN'T WORK FOR EDGE CASES
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
    if pivot_ix is None:
        return _binsearch(nums, target)
    # return _binsearch(nums[pivot_ix + 1:], target) + pivot_ix + 1 if _binsearch(nums[pivot_ix + 1:], target) != -1 else -1
    if nums[0] > target:
        return _binsearch(nums[pivot_ix + 1:], target) + pivot_ix + 1 if _binsearch(nums[pivot_ix + 1:], target) != -1 else -1
    elif nums[0] < target:
        return _binsearch(nums[:pivot_ix + 1], target) + pivot_ix + 1 if _binsearch(nums[pivot_ix + 1:], target) != -1 else -1
    else:
        return 0


if __name__ == '__main__':
    # print(search_working([4, 5, 6, 7, 0, 1, 2], 0))
    # print(search_working([1, 3], 1))
    # print(search_working([3, 1], 1))
    # print(search_working([4, 5, 6, 7, 0, 1, 2], 3))
    # print(search_working([3, 5, 1], 3))
    print(search_working([3, 5, 1], 5))
