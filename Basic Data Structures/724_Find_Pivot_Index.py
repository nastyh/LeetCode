def pivotIndex(nums):  # O(n) and O(n)
    """
    Create a list with running sums. Element at index i there means the sum of all elements to the left including the i-th element
    Iterate through the list and check if this element minus the i-th element (it will give the sum of all elements to the left)
    is equal to the last dp's element minus the i-th element in dp (it will give the sum of all elements to the right)
    """
    if len(nums) == 0: return -1
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = dp[i - 1] + nums[i]
    for i in range(len(nums)):
        if dp[i] - nums[i] == dp[-1] - dp[i]:
            return i
    return -1
    

def pivotIndex_alt(nums):  # O(n) and O(1)
    """
    Same but without building dp
    """
    all_sum = sum(nums)
    l_sum = 0
    for k, v in enumerate(nums):
        if l_sum == all_sum - l_sum - v:
            return k
        l_sum += v
    return -1


def pivotIndex_another(nums):  # O(n) both 
    """
    with two running sums.
    from_left is the running sums from the left
    from_right is the running sums from the right
    then start comparing element by element. If you find the matching element, immediately return it (b/c we need the very first match)
    """
    res = -1
    if len(nums) == 0: return res
    from_left, from_right = [None] * len(nums), [None] * len(nums)
    from_left[0] = nums[0]
    from_right[-1] = nums[-1]
    for i in range(1, len(nums)):
        from_left[i] = from_left[i - 1] + nums[i]
    for j in range(len(nums) - 2, -1, -1):
        from_right[j] = from_right[j + 1] + nums[j]
    for k in range(len(nums)):
        if from_left[k] == from_right[k]:
            res = k
            break
    return res


if __name__ == '__main__':
    print(pivotIndex([1, 7, 3, 6, 5, 6]))
    print(pivotIndex([1, 2, 3]))
    print(pivotIndex([-1, -1, 0, 0, -1, -1]))
    print(pivotIndex_alt([1, 7, 3, 6, 5, 6]))
    print(pivotIndex_alt([1, 2, 3]))
    print(pivotIndex_alt([-1, -1, 0, 0, -1, -1]))
    print(pivotIndex_another([1, 7, 3, 6, 5, 6]))
    print(pivotIndex_another([1, 2, 3]))
    print(pivotIndex_another([-1, -1, 0, 0, -1, -1]))