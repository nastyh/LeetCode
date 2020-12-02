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

def pivotIndex_alt(nums):
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


if __name__ == '__main__':
    print(pivotIndex([1, 7, 3, 6, 5, 6]))
    print(pivotIndex([1, 2, 3]))
    print(pivotIndex_alt([1, 7, 3, 6, 5, 6]))
    print(pivotIndex_alt([1, 2, 3]))