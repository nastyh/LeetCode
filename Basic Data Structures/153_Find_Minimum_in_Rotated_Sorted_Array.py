def findMin(nums):
    def _findpivot(nums):
        piv_ix = None
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                piv_ix = i
                break
        return piv_ix
    piv_ix = _findpivot(nums)
    if piv_ix is None:
        return nums[0]
    elif piv_ix == len(nums) - 1:
        return nums[0]
    else:
        return nums[piv_ix + 1]


def findMin_bin_search(nums):
    if len(nums) == 1: return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] > nums[m + 1]:
            return nums[m + 1]
        if nums[m - 1] > nums[m]:
            return nums[m]
        if nums[m] > nums[0]:
            l = m + 1
        else:
            r = m - 1


def findMin_bin_search_alt(nums):
    left, right = 0, len(nums) - 1
    while nums[left] > nums[right]:
        middle  = (left + right) // 2
        if nums[middle] < nums[right]:
            right = middle
        else:
            left = middle + 1
    return nums[left]


if __name__ == '__main__':
    print(findMin([3, 4, 5, 1, 2]))