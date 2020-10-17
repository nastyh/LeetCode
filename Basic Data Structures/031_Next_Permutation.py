def nextPermutation(nums):
    i = 0
    for i in range(len(nums)-1,0,-1):
        if nums[i] > nums[i-1]:
            break
    i-=1
        # Get the next larger element.
    temp = [j for j in nums[i:] if j > nums[i]]

        # No Larger element is there. Simply return the sorted array.
    if not temp:
        nums.reverse()
    else:
        #Swap the element with the larger element and sort the rest of the array.
        just_large = min(temp)
        ind = nums[i:].index(just_large) + i
        nums[i], nums[ind] = nums[ind], nums[i]
        nums[:] = nums[:i + 1] + sorted(nums[i + 1:])
    return nums


if __name__ == '__main__':
    print(nextPermutation([1,2,3]))
