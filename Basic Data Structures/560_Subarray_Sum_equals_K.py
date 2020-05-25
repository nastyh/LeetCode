def subarraySum(nums, k):
        res, curr_sum, start = 0, 0, nums[0]
        for i in range(1, len(nums)):
            curr_sum = start + nums[i]
            if curr_sum == k:
                res += 1
                start = nums[i]
        return res


def subarraySum(nums, k):
    count = s = 0
    Map = {}
    Map[0] = 1
    for i in range(len(nums)):
        s += nums[i]
        if s - k in Map:
            count += Map.get(s-k)
        Map[s] = Map.get(s,0) +1
    return count

def subarraySum(nums, k):
    count = 0
    for start in range(len(nums)):
        sum = 0
        for end in range(start, len(nums)):
            sum += nums[end]
            if sum == k:
                count += 1
    return count


if __name__ == '__main__':
    print(subarraySum([1,1,1], 2))
