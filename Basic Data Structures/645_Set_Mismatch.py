from collections import Counter
def findErrorNums(nums):  # O(n) and O(1)
    for x in nums: 
        x = abs(x)
        if nums[x - 1] < 0:
            dup = x
        nums[x - 1] *= -1
    missing = next(i for i, x in enumerate(nums, 1) if x > 0 and i != dup)
    return [dup, missing]


def findErrorNums_sort(nums):  # O(nlogn) and O(1)
    dup, missing = 0, 0
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            dup = nums[i]
    missing = (lambda x: x * (x + 1) // 2)(len(nums)) - sum(nums) + dup
    return [dup, missing]


def findErrorNums_dict(nums):  # O(n) both 
    d = Counter(nums)
    dup, missing = 0, 0 
    for k, v in d.items():
        if v > 1:
            dup = k
    missing = (lambda x: x * (x + 1) // 2)(len(nums)) - sum(nums) + dup
    return [dup, missing]


def findErrorNums_another(nums):  # O(n) both 
    """
    Dup is easy to find using a dictionary
    Missing is sum of all numbers from 1 to n including minus sum of nums and we need to add back dup b/c we went too low
    """
    n = len(nums)
    d = Counter(nums)
    dup, missing = 0, 0 
    all_nums = [i for i in range(1, n + 1)]
    for k, v in d.items():
            if v > 1:
                dup = k
    missing = sum(all_nums) - sum(nums) + dup
    return [dup, missing]


def findErrorNums_xor(nums):  # O(n) and O(1)
    """
    by xor-ing all the numbers of the list together with all the numbers of the list as a set (removing the duplicate) we get the duplicated number
    we end up xoring all elements twice which will turn into zero (i ^ i = 0) and one extra time with the duplicated number so we will get 0 ^ duplicated = duplicated
    by xor-ing all the numbers of the list once together with the numbers from 1 to n we get the missing number
    0 ^ missing = missing
    """
    xor, duplicated_num, missing_num = 0, 0, len(nums)
    for num in set(nums):
        xor ^= num
    for num in nums:
        duplicated_num ^= num 
        for i in range(1, len(nums)):
        missing_num ^= i
    return [duplicated_num ^ xor, missing_num ^ xor]