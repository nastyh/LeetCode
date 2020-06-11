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
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([3,1,3,4,2]))
    print(findDuplicate_set([1,3,4,2,2]))
    print(findDuplicate_set([3,1,3,4,2]))
    print(findDuplicate_weird([1,3,4,2,2]))
    print(findDuplicate_weird([3,1,3,4,2]))
