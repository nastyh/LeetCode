from collections import deque
def maxSlidingWindow(nums, k): # TLE, O(Nk) and O(N - k + 1) for the answer
    if len(nums) == 0: return []
    res = []
    for l in range(len(nums) - k + 1):
        curr = nums[l:l + k]
        res.append(max(curr))
    return res


def maxSlidingWindow_sliding(nums, k): #sliding window
    if len(nums) == 0: return []
    l = 0
    r = l + k - 1
    res = []
    while r < len(nums):
        curr_l = nums[l:r + 1]
        res.append(max(curr_l))
        l += 1
        r += 1
    return res


def maxSlidingWindow_deque(nums, k):  # O(n) and O(n)
    """
    deque allows to access the corner elements in O(1)
    Keep only the indices of elements from the current sliding window
    Remove indices of all elements smaller than the current one, since they won't be an answer
    Append the current element to the deque
    Append the most left element of the deque to res (b/c we've built a non-increasing deque essentially)
    """
    if len(nums) <= 1: return nums
    res = []
    d = deque()
    for i in range(len(nums)):
        while d and nums[i] >= nums[d[-1]]:
            d.pop()
        d.append(i)
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            res.append(nums[d[0]])
    return res


def maxSlidingWindow_dp(nums, k):  # O(n) both
    n = len(nums)
    if n * k == 0:
        return []
    if k == 1:
        return nums
    left = [0] * n
    left[0] = nums[0]
    right = [0] * n
    right[n - 1] = nums[n - 1]
    for i in range(1, n):
        # from left to right
        if i % k == 0:
            # block start
            left[i] = nums[i]
        else:
            left[i] = max(left[i - 1], nums[i])
        # from right to left
        j = n - i - 1
        if (j + 1) % k == 0:
            # block end
            right[j] = nums[j]
        else:
            right[j] = max(right[j + 1], nums[j])
    output = []
    for i in range(n - k + 1):
        output.append(max(left[i + k - 1], right[i])) 
    return output


if __name__ == '__main__':
    # print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # print(maxSlidingWindow_sliding([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # print(maxSlidingWindow_deque([1, 3, -1, -3, 5, 3, 6, 7], 3))
