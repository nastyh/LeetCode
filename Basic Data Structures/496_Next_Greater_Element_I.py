def nextGreaterElement(nums1, nums2): # brute force
    res = [-1] * len(nums1)
    for ix in range(len(nums1)):
        if nums1[ix] in nums2:
            for j in range(nums2.index(nums1[ix]), len(nums2)):
                if nums2[j] > nums1[ix]:
                    res[ix] = nums2[j]
                    break
    return res

def nextGreaterElement_brute_force_another(nums1, nums2):
    """
    to avoid reusing .index(), keep a dictionary
    {element in the first array: its index in the second array}
    """
    res = [-1] * len(nums1)
    d = {}
    for num in nums1:
        d[num] = nums2.index(num)
    for k, v in enumerate(nums1):
        for key in range(d[v] + 1, len(nums2)):
            if nums2[key] > v:
                res[k] = nums2[key]
                break
    return res

def nextGreaterElement_alt(nums1, nums2):
    """
    Build a dictionary d:
    {element in nums2: next greater element to the right}
    If there is not greater element for a number, then there won't be a respective pair
    """
    d, st = {}, []
    res = [-1] * len(nums1)
    for num in nums2:
        while st and st[-1] < num:
            d[st.pop()] = num
        st.append(num)
    for k, v in enumerate(nums1):
        if v in d:
            res[k] = d[v]
    return res


    # Just an experiment; isn't required for this question
def _helper(nums2): # return the next larger element to the right from a given element
    res = []
    st = []
    for i in range(len(nums2)):
        if len(st) == 0:
            st.append(nums2[i])
        else:
            while st and st[-1] < nums2[i]:
                res.append(nums2[i])
                st.pop()
            st.append(nums2[i])
    if len(res) != len(nums2):
        res.extend([-1 for i in range(len(nums2) - len(res))])
    return res

if __name__ == '__main__':
    # print(nextGreaterElement([4, 1 ,2], [1, 3, 4, 2]))
    # print(nextGreaterElement([2, 4], [1, 2, 3, 4])) 
    print(nextGreaterElement_alt([2, 4], [1, 2, 3, 4]))   
    print(nextGreaterElement_alt([4, 1, 2], [1, 3, 4, 2]))
    print(nextGreaterElement_alt([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))
    print(_helper([6, 10, 8, 5, 2, 11, 12, 4, 20]))