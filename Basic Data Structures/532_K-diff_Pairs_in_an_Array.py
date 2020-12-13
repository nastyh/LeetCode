from collections import Counter
def findPairs(nums, k):  # O(n) and O(n)
    counter = Counter(nums)
    result = 0
    if k > 0:
        result = sum(1 for x in counter if x + k in counter)
    else:
        result = sum(1 for x in counter if counter[x] > 1)
    return result


def findPairs_brute_force(nums, k):  # O(n^2) times out
    nums.sort()
    res = 0
    for l in range(len(nums) - 1):
        if l > 0 and nums[l - 1] == nums[l]:
            continue
        for r in range(l + 1, len(nums)):
            if r > l + 1 and nums[r - 1] == nums[r]:
                continue
            if abs(nums[l] - nums[r]) == k:
                res += 1
    return res


def findPairs_binary_search(nums, k):
    nums.sort()
    cnt = 0
    for i in range(len(nums)):
        if i > 0:
            if nums[i] == nums[i - 1]:
                continue
        low = i + 1
        right = len(nums) - 1
        while low <= right:
            mid = low + (right - low) // 2
            if nums[mid] == nums[i] + k:
                cnt += 1
                break
            elif nums[mid] < nums[i] + k:
                low = mid + 1
            else:
                right = mid - 1
    return cnt



if __name__ == '__main__':
    print(findPairs([3, 1, 4, 1, 5], 2))
    print(findPairs([1, 2, 3, 4, 5], 1))
    print(findPairs([1, 3, 1, 5, 4], 0))
    print(findPairs([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3))
    print(findPairs([-1. -2, -3], 1))
    print(findPairs_brute_force([3, 1, 4, 1, 5], 2))
    print(findPairs_brute_force([1, 2, 3, 4, 5], 1))
    print(findPairs_brute_force([1, 3, 1, 5, 4], 0))
    print(findPairs_brute_force([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3))
    print(findPairs_brute_force([-1. -2, -3], 1))