def checkSubarraySum(nums, k):
    for i in range(len(nums)):
        if nums[i:i + 2] == [0,0]:
            return True

    if k == 0 or len(nums) < 2:
        return False

    sum_mod_dict = {}
    for i in range(len(nums) + 1):
        sum_mod = sum(nums[:i]) % k
        if sum_mod in sum_mod_dict.keys():
            if sum_mod_dict[sum_mod] < i - 1:
                return True
            else:
                continue
        sum_mod_dict[sum_mod] = i
    return

def checkSubarraySum_alt(nums, k):
    mp = {0: -1}
    prefix_sum = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        if k != 0:
            prefix_sum = prefix_sum % k
        if prefix_sum in mp:
            # I know that sum between mp[prefix_sum] + 1 and i is multiple of K, so I don't have to include mp[prefix_sum]
            if i - mp[prefix_sum] > 1:
                return True
        else:
            # if prefix_sum doesn't exists, then add its index, otherwise don't update it, i would always prefer to keep the
            # oldest index, so that I can get length of atleast 2
            mp[prefix_sum] = i

    return False


if __name__ == '__main__':
    print(checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(checkSubarraySum_alt([23, 2, 4, 6, 7], 6))
