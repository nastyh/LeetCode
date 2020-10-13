def removeDuplicates(nums):  # easiest to follow
    if len(nums) <= 1: return len(nums)
    l, r = 0, 1
    while r < len(nums):
        if nums[l] == nums[r]:
            r += 1
        else:
            l += 1
            nums[l] = nums[r]
    return l + 1


def removeDuplicates(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1

        # nums = [0,0,1,1,1,2,2,3,3,4]
    j = 1 # slow pointer, only move when meets a unique number
    for i in range(1, len(nums)): # faster pointer, i will iterate over all element in nums
        if nums[i] != nums[i-1]: # when nums[i] is a unique number, assign it to nums[j]
            nums[j] = nums[i]
            j += 1
        # after for loop, i = 9, j = 5, nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        # we can see the nums[:5] is the unique number list we want
    return j
    

def removeDuplicates(nums):
    head = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[head]:
            head += 1
            nums[head] = nums[i]
    return head + 1


if __name__ == '__main__':
    print(removeDuplicates([0, 0, 0, 1, 2, 3, 3, 4]))
