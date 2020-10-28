def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums2_index=0
    nums1_index = 0
    while nums2_index < n and nums1_index < m:
        if nums2[nums2_index] <= nums1[nums1_index]:
            nums1.insert(nums1_index, nums2[nums2_index])
            m += 1
            nums2_index += 1
        nums1_index += 1
    while nums2_index < n:
        nums1.insert(m, nums2[nums2_index])
        m += 1
        nums2_index += 1
    for _ in range(n):
        nums1.pop()


def merge_another(nums1, m, nums2, n):
    while len(nums1)!=m:
        nums1.pop()
    for i in nums2:
        nums1.append(i)
    nums1.sort()


def merge_back((nums1, m, nums2, n):
    m -= 1
    n -= 1
    for i in range(len(nums1) - 1, -1, -1):
        if n < 0: # whatever remains in nums1 are smaller than all elems in nums2
            return
        if m < 0: # copy those in nums2 smaller than all elems in nums1 to the start of nums1
            for j in range(n, -1, -1):
                nums1[j] = nums2[j]
            return
        if nums1[m] >= nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1


    # res = [None] * (m + n)
    # i, j, k = 0, 0, 0

    # while i < m and j < n:
    #     if nums1[i] <= nums2[j]:
    #         res[k] = nums1[i]
    #         i += 1
    #         k += 1
    #     else:
    #         res[k] = nums2[j]
    #         j += 1
    #         k += 1

    # while i < m:
    #     res[k] = nums1[i]
    #     i += 1
    #     k += 1

    # while j < n:
    #     res[k] = nums2[j]
    #     j += 1
    #     k += 1

    # return res

