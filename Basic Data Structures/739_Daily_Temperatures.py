def dailyTemperatures(T): # brute force, O(n^2)
    if len(T) == 1: return 0
    res = [None] * len(T)
    res[-1] = 0
    for i in range(len(T) - 1):
        for j in range(i, len(T)):
            if T[j] > T[i]:
                res[i] = j - i
                break
            else:
                res[i] = 0
    return res


def dailyTemperatures_one_pass(T):
    res = [0] * len(T)
    res[-1] = 0
    st = []
    st.append((T[-1], len(T) - 1))
    for i in range(len(T) - 2, -1, -1):
        while st and st[-1][0] <= T[i]:
            st.pop()
        if st and st[-1][0] > T[i]:
            res[i] = st[-1][1] - i
        st.append((T[i], i))
    return res


def dailyTemperatures_stack(nums):
    """
    start from the end
    Add tuples (value, index) to the stack if the stack is empty.
    If the current element is more than the last element in the stack, remove the last element and append the current instead
    If the current element in less than the last element, it means that res[i] should become equal to the index from the tuple that is the last element of the stack minus the current
    value's index (b/c we need a distance)
    This way, we are maintaining an increasing sequence (from left to right)
    """
    res, st = [0] * len(nums), []
    for i in range(len(nums) - 1, -1, -1):
        while st and nums[i] >= st[-1][0]:
            st.pop()
        if st and nums[i] < st[-1][0]:
            res[i] = st[-1][1] - i 
        st.append((nums[i], i))
    return res

if __name__ == '__main__':
    # print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # print(dailyTemperatures_one_pass([73, 74, 75, 71, 69, 72, 76, 73]))   
    # print(dailyTemperatures_one_pass([55, 38, 53, 81, 61, 93, 97, 32, 43, 78])) 
    print(dailyTemperatures_stack([73, 74, 75, 71, 69, 72, 76, 73]))