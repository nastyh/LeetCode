
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
    print(subarraySum_d([1,2,3], 3))
    print(subarraySum_another([1,2,3], 3))
