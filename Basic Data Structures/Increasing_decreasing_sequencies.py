def NGE_brute_force(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [-1]
    res = [-1] * len(nums)
    for i in range(len(nums) - 1):
        for n in nums[i + 1:]:
            if n > nums[i]:
                res[i] = n
                break
    return res


def NGE(nums):
    res = []
    st = []
    for i in range(len(nums)):
        if len(st) == 0:
            st.append(nums[i])
        else:
            while st and st[-1] < nums[i]:
                res.append(nums[i])
                st.pop()
            st.append(nums[i])
    if len(res) != len(nums):
        res.extend([-1 for i in range(len(nums) - len(res))])
    return res


def NGE_alt(nums):
    res = [-1] * len(nums)
    st = []
    for i in range(len(nums)):
        while st and nums[i] > nums[st[-1]]:
            res[st.pop()] = nums[i]
        st.append(i)
    return res


def NSE_alt(nums):
    res = [-1] * len(nums)
    st = []
    for i in range(len(nums)):
        while st and nums[i] < nums[st[-1]]:
            res[st.pop()] = nums[i]
        st.append(i)
    return res


def non_decreasing(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return nums
    res, st = [], []
    res.append(nums[0])
    st.append(nums[0])
    for i in range(1, len(nums)):
        # if len(st) == 0:
        #     st.append(nums[i])
        while st and nums[i] > st[-1]:
            res.append(nums[i])
            st.pop()
        st.append(nums[i])
    return res


if __name__ == '__main__':
    print(NGE_brute_force([6, 10, 8, 5, 2, 11, 12, 4, 20]))
    print(NGE([6, 10, 8, 5, 2, 11, 12, 4, 20]))
    print(NGE_alt([6, 10, 8, 5, 2, 11, 12, 4, 20]))
    print(NSE_alt([6, 10, 8, 5, 2, 11, 12, 4, 20]))
    print(NGE_alt([6, 1, 4, 8]))
    # print(non_decreasing([6, 10, 8, 5, 2]))
    # print(non_decreasing([6, 10, 8, 5, 2, 11, 12, 4, 20]))
    # print(non_decreasing([10, 9, 8, 7]))
    # print(non_decreasing([6, 6, 6, 6]))
    # print(non_decreasing([2]))
    # print(non_decreasing([]))
