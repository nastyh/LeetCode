import heapq
def medianSlidingWindow(nums, k): # Brute Force, very slow
    if len(nums) == 0: return None
    l, r, res = 0, k, []
    while r <= len(nums):
        t = sorted(nums[l:r])
        if len(t) % 2 == 1:
            res.append(t[len(t) // 2])
        else:
            r_ix = len(t) // 2
            m = (t[r_ix - 1] + t[r_ix]) / 2
            res.append(m)
        l += 1
        r += 1
    return res

# def medianSlidingWindow_heaps(nums, k): # with two heaps
#     if len(nums) == 0: return None
#     l, r, res, lh, rh = 0, k, [], [], []
#     while r <= len(nums):
#         t = nums[l:r]
#         lh = t[:len(t) // 2 + 1]
#         lh = lh * (-1)
#         rh = t[len(t) // 2:]
#         heapq.heapify(lh)
#         heapq.heapify(rh)
#         res.append( (heapq.heappop(lh) * (-1) + heapq.heappop(rh)) / 2 )
#         l += 1
#         r += 1
#         # heapq.heappush(lh, nums[])
#     return res



if __name__ == '__main__':
    print(medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(medianSlidingWindow([1,4,2,3], 4))
    # print(medianSlidingWindow_heaps([1,3,-1,-3,5,3,6,7], 3))
