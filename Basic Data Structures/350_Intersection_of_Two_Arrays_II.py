from collections import Counter
def intersect(nums1, nums2):  # straigthforward
    if len(nums1) <= len(nums2):
        short = nums1
        long = nums2
    else:
        short = nums2
        long = nums1

    res = []
    for i in short:
        if i in long:
            res.append(i)
            long.remove(i)
    return res


def intersect_dict(nums1, nums2):  # a bit faster but uses extra space
    res = []
    if len(nums1) <= len(nums2):
        shorter = nums1
        longer = nums2
    else:
        shorter = nums2
        longer = nums1
    d_short = Counter(shorter)
    d_long = Counter(longer)
    for k in shorter:
        if d_long.get(k, 0) != 0:
            res.append(k)
            d_long[k] -= 1
    return res


if __name__ == '__main__':
    print(intersect([1, 2, 2, 1], [2, 2]))
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersect_dict([1, 2, 2, 1], [2, 2]))
    print(intersect_dict([4, 9, 5], [9, 4, 9, 8, 4]))
