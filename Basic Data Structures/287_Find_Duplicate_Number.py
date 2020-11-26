def findDuplicate_best(nums):
    """
    Go through elements. They will serve as indices to other elements in this list
    Every time multiply nums[num] by -1.
    If you hit a number than is already negative, return it. 
    The logic is that if it's negative, it means you've already seen a number that served as an index
    and brought you to this number, and you multiplied it by -1. Hence, it's a duplicate
    """
    for k, num in enumerate(nums):
        if nums[abs(num)] < 0: 
            return abs(nums[k])
        nums[abs(num)] *= - 1

def findDuplicate(nums): # using sort, nlog(n)
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

def findDuplicate_set(nums): # using a set
    s = set()
    for num in nums:
        if num not in s:
            s.add(num)
        else:
            return num

def findDuplicate_weird(nums):
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


if __name__ == '__main__':
    print(findDuplicate_best([1, 3, 4, 2, 2]))
    print(findDuplicate_best([3, 1, 3, 4, 2]))
    print(findDuplicate([1, 3, 4, 2, 2]))
    print(findDuplicate([3, 1, 3, 4, 2]))
    print(findDuplicate_set([1, 3, 4, 2, 2]))
    print(findDuplicate_set([3, 1, 3, 4, 2]))
    print(findDuplicate_weird([1, 3, 4, 2, 2]))
    print(findDuplicate_weird([3, 1, 3, 4, 2]))
