def moveZeroes_latest(nums):
    """
    Make two pointers 
    l points to cells where a zero sits. Eventually this spot should get a non-zero number
    If we found the right spot (nums[l] == 0),
    we make a decision,
    if nums[r] is a non-zero number, we have everything for a swap
    Make this swap and move both pointers forward 
    If nums[r] is a zero, it's not good, keep looking by moving r
    Finally we have a case when nums[l] != 0. Then we need to leave this cell by moving l and move r in order to keep the process going
    """
    l, r = 0, 0
    while r < len(nums):
        if nums[l] == 0:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1
        else:
            l += 1
            r += 1


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

def moveZeroes_another(nums):
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
