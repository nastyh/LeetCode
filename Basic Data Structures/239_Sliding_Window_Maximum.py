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


if __name__ == '__main__':
    # print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # print(maxSlidingWindow_sliding([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # print(maxSlidingWindow_deque([1, 3, -1, -3, 5, 3, 6, 7], 3))
