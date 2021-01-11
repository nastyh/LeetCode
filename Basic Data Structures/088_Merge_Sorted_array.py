def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums2_index = 0
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


def merge_optimal(nums1, m, nums2, n):
    end_of_zeroes = n - 1  # index of the last element in nums2
    end_of_nums = m - 1  #  index of the last non-zero element in nums1
    for i in range(m + n - 1, -1, -1):
        if end_of_nums < 0:
            break
        if nums1[end_of_zeroes] > nums2[end_of_nums]:
            nums1[i] = nums[end_of_nums]
            end_of_nums -= 1
        else:
            nums1[i] = nums2[end_of_zeroes]
            end_of_zeroes -= 1
    

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
