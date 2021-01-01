def nextPermutation(nums):
    i = 0
    for i in range(len(nums)-1, 0, -1):
        if nums[i] > nums[i - 1]:
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


def nextPermutation_alt(nums):
    """
    Start from the end and look for the first occurance of nums[r] > nums[r - 1]
    It means we cannot rearrange anything to the right from r b/c the whole list is in the decreasing order
    Thus, we need to rearrange the numbers to the right of nums[r - 1] incl/ itself
    Replace nums[r - 1] with the number that is larger than itself among the numbers in the right section. It will be nums[i]
    Make a swap
    To get the smallest permutation, place the numbers to the right of i in the reversed order 
    """
    def _swap(a, b):  # swaps elements in place
        nums[a], nums[b] = nums[b], nums[a]
        return
    def _rev(i):  # reverses a list from a given index
        nums[i:] = nums[i:][::-1]
    if len(nums) <= 1:  #edge case
        return
    r = len(nums) - 1  #start from the end
    while r > 0 and nums[r - 1] >= nums[r]:  # go to the beginning, while the left element is > than the right element
        r -= 1
    r -= 1  # one extra step to the left 
    while r >= 0:
        i = r + 1
        while i < len(nums) and nums[r] < nums[i]:
            i += 1
        _swap(i - 1, r)
        break
    _rev(i + 1)
    return 


if __name__ == '__main__':
    print(nextPermutation([1, 2, 3]))
    print(nextPermutation_alt([1, 2, 3]))
