def intersection(nums1, nums2):
    if len(nums1) == 0 and len(nums2) == 0:
        return None
    helper, res = [], []
    # helper.append(nums1)
    # helper.append(nums2)
    # helper.sort(key = len)
    # for el in helper[0]:
    #     if el in helper[1]:
    #         if el not in res:
    #             res.append(el)
    # return res

    if len(nums1) < len(nums2):
        l = nums1
        r = nums2
    else:
        l = nums2
        r = nums1

    for el in l:
        if el in r:
            # if el not in res:
            res.append(el)
    return set(res)

# potential additions
def intersection_no_sets(nums1, nums2):
    nums1.sort()
    nums2.sort()
    if not nums1 or not nums2 or len(nums1) < 1 or len(nums2)<1:
        return []
    l, r = 0, 0
    res = []
    while l < len(nums1) and r < len(nums2):
        if nums1[l] == nums2[r]:
            if not res or res[-1] != nums1[l]:
                res.append(nums1[l])
            l += 1
            r += 1
        elif nums1[l] < nums2[r]:
            l += 1
        else:
            r += 1
    return res

if __name__ == '__main__':
    print(intersection([1, 2, 2, 1], [2, 2]))
