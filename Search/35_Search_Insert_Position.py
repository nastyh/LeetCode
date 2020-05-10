def searchInsert(nums, target):
    l, r = 0, len(nums) - 1

    if target <= nums[0]:
        return l
    if target > nums[-1]:
        return r + 1
    if target == nums[-1]:
        return r

    while l < r:
        m_ix = (l + r) // 2
        if nums[m_ix] == target:
            return m_ix
        elif nums[m_ix] < target:
            l = m_ix
        else:
            r = m_ix
        if l + 1 == r:
            return l + 1




if __name__ == '__main__':
    print(searchInsert([1,3,5,6], 5))
