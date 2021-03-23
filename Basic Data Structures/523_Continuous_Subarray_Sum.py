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

def checkSubarraySum_optimal(nums, k): # O(n) both
    """
    make 0 as -1, now we have to find subarray sum equals 0 
    """
    sum_map = {0: -1}
    running_sum = 0
    for index, num in enumerate(nums):
        running_sum += num
        if k != 0:
            running_sum = running_sum % k
        if running_sum in sum_map and index - sum_map[running_sum] > 1:
            return True
        
        if not running_sum in sum_map:
            sum_map[running_sum] = index
    return False

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


def checkSubarraySum_scan(nums, k):  # brute force 
    if len(nums) < 2: return False
    if all(i == 0 for i in nums) and k == 0: return True 
    window = 2
    while window < len(nums):
        l = 0
        r = l + window - 1
        while r < len(nums):
            try:
                if sum(nums[l: r + 1]) % k == 0:
                    return True
            except ZeroDivisionError:
                return False 
            r += 1
        window += 1
    return False 


if __name__ == '__main__':
    print(checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(checkSubarraySum_alt([23, 2, 4, 6, 7], 6))
    print(checkSubarraySum_scan([23, 2, 4, 6, 7], 6))
    print(checkSubarraySum_scan([23, 2, 6, 4, 7], 6))
