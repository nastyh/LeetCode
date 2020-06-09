def moveZeroes(nums):


    for num in nums:
        if num == 0:
            ix = nums.index(num)
            nums.append(num)
            del nums[ix]
    return nums

def moveZeroesTwoPointer(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != 0 and nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        if nums[i] != 0:
            i += 1
    return nums

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0                   # start from 0 (forward pointer)
    j = len(nums) - 1       # start from end (backward pointer)
    while(i<j):
        if nums[i] ==0:
            nums.pop(i)
            nums.insert(j, 0)
            j -= 1
        else:
            i += 1
    return nums


def moveZeroes_brute_force(nums):
    orig_len = len(nums)
    for ix in range(orig_len):
        if nums[ix] == 0:
            nums.remove(nums[ix])
            nums.append(0)

    return nums

if __name__ == '__main__':
    print(moveZeroes_brute_force([0,1,0,3,12]))
    print(moveZeroesTwoPointer([0,1,0,3,12,0,0]))
    print(moveZeroes_brute_force([0,1,0,3,12,0,0]))
