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



if __name__ == '__main__':
    print(intersection([1,2,2,1], [2,2]))
