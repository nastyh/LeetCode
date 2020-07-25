
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
    d, curr_sum, res = {0:1}, 0, 0
    for num in nums:
        curr_sum += num
        if curr_sum - k in d:
            res += d[curr_sum - k]
        if curr_sum in d:
            d[curr_sum] += 1
        else:
            d[curr_sum] = 1
    return res

def subarraySum_another(nums, k):
    count = 0
    for start in range(len(nums)):
        sum = 0
        for end in range(start, len(nums)):
            sum += nums[end]
            if sum == k:
                count += 1
    return count


if __name__ == '__main__':
    print(subarraySum_d([1, 2, 3], 3))
    print(subarraySum_dict([3, 4, 7, 2, -3, 1, 4, 2], 7))
    print(subarraySum_dp([3, 4, 7, 2, -3, 1, 4, 2], 7))
    print(subarraySum_dp([1, 1, 1], 2))
    print(subarraySum_dp([1, -1, 5 ,-2, 3], 3))
    print(subarraySum_another([1, 1, 1], 2))
    print(subarraySum_another([1, 1, 1, 2], 2)) # [1,2,3], 3
