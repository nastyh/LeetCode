def missingNumber(nums): # O(n) and O(n)
    d = dict.fromkeys(range(min(nums), len(nums) + 1))
    for n in nums:
        if n in d:
            d[n] = 1
    return [k for k, v in d.items() if v is None][0]


def missingNumber_alt(nums):  # O(n) to xor the whole array and O(1)
    """
    numbers are in the range [0, n - 1]
    n replaces the missing number in nums
    if we initialize a variable to len(nums) and XOR it will all indices and values of elements,
    we'll be left with the missing number 
    """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


def missingNumber_Gauss(nums):  # O(n) to compute sum(nums) and O(1)
    """
    Sum of the arithmetic progression is (a_1 + a_n) * n / 2
    where a_1 is the first element of the progression  (in our case it's always 0)
    a_n is the last element of the progression (in our case it's always len(nums))
    n is the number of elements in the progression  (it's len(nums) + 1 b/c we need to account for a zero)
    Then subtact the actual sum(nums) from it
    """
    s = (0 + len(nums)) * (len(nums) + 1) / 2
    return int(s - sum(nums))


def missingNumber_naive(nums):  # O(n^2) and O(n)
    full = range(0, len(nums) + 1)
    for n in full:
        if n not in nums:
            return n


def missingNumber_sorting(nums):  # O(nlogn) and O(1)
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i + 1]:
            return nums[i] + 1
    if nums[-1] != len(nums):  # edge cases
        return len(nums)
    else:
        return 0


if __name__ == '__main__':
    print(missingNumber([3, 0, 1]))
    print(missingNumber([0]))
    print(missingNumber_Gauss([3, 0, 1]))
    print(missingNumber_Gauss([0]))
    print(missingNumber_naive([0]))
