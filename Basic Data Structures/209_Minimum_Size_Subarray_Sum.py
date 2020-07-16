import math
def minSubArrayLen(s, nums):
    if len(nums) == 0: return 0
    l, r = 0, 0
    curr, glob, curr_sum = 0, math.inf, 0

    # curr_sum = nums[l]
    while r < len(nums):
        curr_sum += nums[r]
        while curr_sum >= s:
            curr = r - l + 1
            glob = min(glob, curr)
            curr_sum -= nums[l]
            l += 1
        r += 1

    return glob if glob != math.inf else 0

def minSubArrayLen_alt(s, nums): # pretty much the same but list slicing looks more Pythonic; way slower, though
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

if __name__ == '__main__':
    print(minSubArrayLen(7, [2,3,1,2,4,3]))
    print(minSubArrayLen(11, [1,2,3,4,5]))
    print(minSubArrayLen_alt(11, [1,2,3,4,5]))
    print(minSubArrayLen_alt(7, [2, 3, 1, 2, 4, 3]))

