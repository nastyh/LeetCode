def containsNearbyAlmostDuplicate(nums, k, t):
    size = len(nums)
    if t == 0 and len(nums) == len(set(nums)):
        return False        
    for i, cur_val in enumerate(nums):  
        for j in range(i + 1, i + k + 1):
            if j >= size:
                break
            if abs(cur_val - nums[j]) <= t:
                return True
    return False


if __name__ == '__main__': 
    print(containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
    print(containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
    print(containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))