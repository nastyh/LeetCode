def numSubarrayProductLessThanK(nums, k):  # O(N) both
    if k <=1: return 0 # edge case, required
    l, r, res, prods = 0, 0, 0, 1
    while r < len(nums):
        prods *= nums[r]
        while l < len(nums) and prods >= k:
            prods /= nums[l]
            l += 1
        if prods < k:
            res += r - l + 1  # need this line in order to account for elements themselves if they're < k
        r += 1
    return res

def numSubarrayProductLessThanK_alt(nums, k):
    l, r, res, prods = 0, 0, 0, 1
    while r < len(nums):
        prods *= nums[r]
        while l < len(nums) and prods >= k:
            prods /= nums[l]
            l += 1
        if prods < k:
            # res += r - l + 1
            res += 1
        r += 1
    return res


if __name__ == '__main__':
    print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(numSubarrayProductLessThanK_alt([10, 5, 2, 6], 100))
