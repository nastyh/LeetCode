def maxSlidingWindow(nums, k): # brute force
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

if __name__ == '__main__':
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(maxSlidingWindow_sliding([1,3,-1,-3,5,3,6,7], 3))
