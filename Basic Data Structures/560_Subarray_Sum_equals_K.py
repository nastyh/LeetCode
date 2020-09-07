
def subarraySum_d(nums, k):
    count = s = 0
    Map = {}
    Map[0] = 1
    for i in range(len(nums)):
        s += nums[i]
        if s - k in Map:
            count += Map.get(s-k)
        Map[s] = Map.get(s,0) +1
    return count

# a bit simpler to follow

def subarraySum_dp(nums, k):
    dp = [None] * len(nums)
    res = 0
    dp[0] = 0
    for ix in range(1, len(nums)):
        dp[ix] = dp[ix - 1] + nums[ix]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if dp[j] - dp[i] == k:
                res += 1
    return res + 1

def subarraySum_dict(nums, k):
    d, curr_sum, res = {0 : 1}, 0, 0
    for num in nums:
        curr_sum += num
        if curr_sum - k in d:
            res += d[curr_sum - k]
        if curr_sum in d:
            d[curr_sum] += 1
        else:
            d[curr_sum] = 1
    return res


def subarraySum_n2(nums, k):  # O(n*2). Two loops. B/c r starts at the same position as l, we account for one-element situations 
    res = 0
    for l in range(len(nums)):
        curr_sum = 0
        for r in range(l, len(nums)):
            curr_sum += nums[r]
            if curr_sum == k:
                res += 1
    return res

def subarraySum_another(nums, k):  # doesn't work for [-1, -1, 1], 0
    if len(nums) == 1:
        if nums[0] == k: return 1
        else: return 0
    curr_sum, res = 0, 0
    l, r = 0, 1
    if any(i == k for i in nums): res += 1
    while r < len(nums):
        curr_sum = sum(nums[l: r + 1])
        if curr_sum == k:
            res += 1
            curr_sum = 0
            l += 1
            r += 1
        else:
            r += 1
    if r == len(nums) - 1:
        while l < len(nums):
            curr_sum = sum(nums[l: r + 1])
            if curr_sum == k:
                res += 1
                l += 1
                curr_sum = 0
            else:
                l += 1
    return res


if __name__ == '__main__':
    print(subarraySum_d([1, 2, 3], 3))
    print(subarraySum_dict([3, 4, 7, 2, -3, 1, 4, 2], 7))
    print(subarraySum_dp([3, 4, 7, 2, -3, 1, 4, 2], 7))
    print(subarraySum_dp([1, 1, 1], 2))
    print(subarraySum_dp([1, -1, 5, -2, 3], 3))
    print(subarraySum_another([1, 1, 1], 2))
    print(subarraySum_another([1, 1, 1, 2], 2)) # [1,2,3], 3
    print(subarraySum_another([1, 2, 3], 3))
    print(subarraySum_n2([1, 2, 3], 3))
    print(subarraySum_n2([-1, -1, 1], 0))