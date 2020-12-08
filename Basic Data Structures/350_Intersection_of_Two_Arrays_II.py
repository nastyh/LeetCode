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

def intersect_sort(nums1, nums2):
    nums1.sort()
    nums2.sort()
    if not nums1 or not nums2 or len(nums1) < 1 or len(nums2)<1:
        return []
    
    l, r = 0, 0
    res = []
    
    while l < len(nums1) and r<len(nums2):
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
    print(intersect([1, 2, 2, 1], [2, 2]))
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersect_dict([1, 2, 2, 1], [2, 2]))
    print(intersect_dict([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersect_sort([4, 9, 5], [9, 4, 9, 8, 4]))