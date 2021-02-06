 def search(nums, target):  # O(logn) and O(1)
    """
    Need to account for possible duplicates standing next to each other
    Keep moving begin and end to the middle till elelements next to them are the same
    After that the main part starts
    First, the best scenario
    Second, nums[mid] > nums[end] means that something's wrong, it shouldn't be like that in a normal sorted array.
    Thus, let's better go to the left part. If target is within the bounds of the left part, do a usual bin search on the left part
    Otherwise, move to the right
    Third, nums[mid] <= nums[end], it means that potentially the right side is normal and sorted.
    Check if target is within the boundaries of the right side. If yes, do a binary search.
    If no, go to the left side
    """
    begin = 0
    end = len(nums) - 1 
    while begin <= end:  
        while begin < end and nums[begin] == nums[begin + 1]:
            begin += 1
        while begin < end and nums[end] == nums[end - 1]:
            end -= 1
        mid = begin + (end - begin) // 2
        if nums[mid] == target:
            return True
        if nums[mid] > nums[end]: # Left side of mid is sorted
            if  nums[begin] <= target < nums[mid]: # Target in the left side
                end = mid - 1
            else: # in right side
                begin = mid + 1
        else: # Right side is sorted
            if  nums[mid] < target <= nums[end]: # Target in the right side
                begin = mid + 1
            else: # in left side
                end = mid - 1
    return False