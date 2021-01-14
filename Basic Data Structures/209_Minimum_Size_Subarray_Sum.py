import math
def minSubArrayLen(s, nums):  # optimal
    if len(nums) == 0: return 0
    l, r = 0, 0
    curr, glob, curr_sum = 0, math.inf, 0
    while r < len(nums):
        curr_sum += nums[r]
        while curr_sum >= s:
            curr = r - l + 1
            glob = min(glob, curr)
            curr_sum -= nums[l]
            l += 1
        r += 1
    return glob if glob != math.inf else 0


def minSubArrayLen_alt(s, nums): # pretty much the same but list slicing looks more Pythonic; way slower, though, b/c we recalculate the whole thing
    l, r, curr_s, curr_l, glob_l = 0, 0, 0, 0, math.inf
    while r < len(nums):
        curr_s = sum(nums[l:r + 1])
        while curr_s >= s:
            curr_l = r - l + 1        
            glob_l = min(glob_l, curr_l)
            l += 1
            curr_s = sum(nums[l:r + 1])          
        r += 1
    return glob if glob != math.inf else 0


def minSubArrayLen_another(s, nums):
    res = math.inf
    if any(x == s for x in nums): return 1
    l, r = 0, 0
    curr, glob, curr_sum = 0, math.inf, 0
    for r in range(len(nums)):
        curr_sum += nums[r]
        while curr_sum >= s:
            glob = min(res, r - l + 1)
            curr_sum -= nums[l]
            l += 1
    return glob if glob != math.inf else 0


def minSubArrayLen_binary(s, nums):  # binary search works b/c the prefix sum is always increasing O(nlogn)
    def bi_search(A, target):
        le, ri = 0, len(A) - 1
        while le <= ri:
            mid = le + (ri - le >> 1)
            if target == A[mid]:
                return mid
            if target < A[mid]:
                ri = mid - 1
            elif target > A[mid]:
                le = mid + 1
        return le
    ret = float('inf')
    # get prefix sum for nums
    cum = [0] * len(nums) + [0]
    cum[0] = 0
    for i in range(1, len(cum)):
        cum[i] = cum[i - 1] + nums[i - 1]
    for le, v in enumerate(cum):
        # use binary search to locate 'ri' index
        ri = bi_search(cum, v + s)
        if ri < len(cum):
            ret = min(ret, ri - le)
    return 0 if ret == float('inf') else ret  


def minSubArrayLen_cum_sum(nums):
    if not nums: return 0
    cum = [0] * (len(nums) + 1)
    cum[0] = 0
    for i in range(1, len(cum)):
        cum[i] = cum[i - 1] + nums[i - 1]
    i, j = 0, 1
    ret = float('inf')
    while j < len(cum):
        while cum[j] - cum[i] >= s:
            ret = min(ret, j - i)
            i += 1
        j += 1
    return 0 if ret == float('inf') else ret
            
            
if __name__ == '__main__':
    print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    # print(minSubArrayLen(11, [1,2,3,4,5]))
    # print(minSubArrayLen_alt(11, [1,2,3,4,5]))
    # print(minSubArrayLen_alt(7, [2, 3, 1, 2, 4, 3]))
    print(minSubArrayLen_another(7, [2, 3, 1, 2, 4, 3]))
    print(minSubArrayLen_binary(7, [2, 3, 1, 2, 4, 3]))

