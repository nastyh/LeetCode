def next_larger_to_the_right(nums2): # return the next larger element to the right from a given element
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
    print(next_larger_to_the_right([3, 2, 4]))
    print(next_larger_to_the_right([5, 4, 3, 10]))
    print(next_larger_to_the_right([6, 7, 8]))
