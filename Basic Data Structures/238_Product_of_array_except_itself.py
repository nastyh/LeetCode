def productExceptSelf(nums):
    ll, rl = [None] * len(nums), [None] * len(nums)
    ll[0], rl[-1] = 1, 1

    for i in range(1, len(ll)):
        ll[i] = ll[i - 1] * nums[i - 1]

    for j in range(len(rl)-2, -1, -1):
        rl[j] = rl[j + 1] * nums[j + 1]

    return [x * y for (x, y) in zip(ll, rl)]

if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))
