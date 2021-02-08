def removeElement(nums, val):  # O(N) and O(1)
    """
    bubble all elements that != val towards the left side of the array 
    Return res b/c it will point to the last bubbled element 
    """
    res = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[res], nums[i] = nums[i], nums[res]
            res += 1
    return res
    

def removeElement_rare(nums, val):  # O(N) and O(1)
    res = 0
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n

