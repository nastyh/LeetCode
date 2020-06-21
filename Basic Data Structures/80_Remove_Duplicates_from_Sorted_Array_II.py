def removeDuplicates(nums):
    length = 0
    for idx, val in enumerate(nums):
        if (length <= 1) or (nums[length - 2] != val):
            nums[length] = val
            length += 1
    return length


if __name__ == '__main__':
    print(removeDuplicates([1,1,1,2,2,3]))

