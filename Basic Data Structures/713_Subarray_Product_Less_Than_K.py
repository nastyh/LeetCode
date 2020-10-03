def numSubarrayProductLessThanK(nums, k):
    l, r, res, prods = 0, 0, 0, 1
    while r < len(nums):
        prods *= nums[r]
        while l < len(nums) and prods >= k:
            prods /= nums[l]
            l += 1
        if prods < k:
            res += r - l + 1
        r += 1
    return res


if __name__ == '__main__':
    print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))