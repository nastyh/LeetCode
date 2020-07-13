def containsNearbyDuplicate(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = i
        else:
            idx_diff = abs(i - d[nums[i]])
            if idx_diff <=k:
                return True
            d[nums[i]] = i
    return False


if __name__ == '__main__':
    print(containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
