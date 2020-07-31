def nextGreaterElement(nums1, nums2): # brute force
    res = [-1] * len(nums1)
    for ix in range(len(nums1)):
        if nums1[ix] in nums2:
            for j in range(nums2.index(nums1[ix]), len(nums2)):
                if nums2[j] > nums1[ix]:
                    res[ix] = nums2[j]
                    break
    return res

def nextGreaterElement_alt(nums1, nums2):
    d = {}
    st = []
    for n in nums2:
        while st and st[-1] < n:
            d[st.pop()] = n 
        st.append(n)
    for i in range(len(nums1)):
        nums1[i] = d.get(nums1[i], -1)
    return nums1


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