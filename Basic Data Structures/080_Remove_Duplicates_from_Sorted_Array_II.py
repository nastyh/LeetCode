def removeDuplicates(nums):  # O(N) and O(1)
    """
    l points to the place where to put the new value
    It's the right place if l is either 0 or 1 or if the element 2 steps back isn't equal to current num
    Then put the value and move l to the right
    """
    l = 0
    for i in range(len(nums)):
        if (l <= 1) or (nums[l - 2] != nums[i]):
            nums[l] = nums[i]
            l += 1
    return l


def removeDuplicates_brute_force(nums):  # O(n^2) and O(1)
    i, count = 1, 1
    # Start from the second element of the array and process
    # elements one by one.
    while i < len(nums):
        # If the current element is a duplicate, 
        # increment the count.
        if nums[i] == nums[i - 1]:
            count += 1
            # If the count is more than 2, this is an
            # unwanted duplicate element and hence we 
            # remove it from the array.
            if count > 2:
                nums.pop(i)   
                # Note that we have to decrement the
                # array index value to keep it consistent
                # with the size of the array.
                i-= 1
        else: 
            # Reset the count since we encountered a different element
            # than the previous one
            count = 1
        # Move on to the next element in the array
        i += 1          
    return len(nums)


if __name__ == '__main__':
    print(removeDuplicates([1,1,1,2,2,3]))

