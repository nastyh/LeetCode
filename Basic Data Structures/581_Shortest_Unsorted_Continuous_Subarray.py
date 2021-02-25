def findUnsortedSubarray(nums):  # O(n) and O(1)
    """
    Find point from the left where the array is definitely unsorted (nums[l] < nums[l - 1]
    Find the minimum from that point l till the end of the array
    Find point from the right where the array is definitely unsorted (nums[r] > nums[r + 1])
    Find the maximum from that point r till the start of the array
    Find index i from the left where our current minimum should go (where nums[i] > minimum)
    Find index j from the right where our current maximum should go (where nums[j] < maximum)
    return j - i + 1 if j - i > 0 else 0
    """
    n = len(nums)
    if n == 1: 
        return 0
    l = 1
    while l < n - 1 and nums[l] > nums[l - 1]:
        l += 1
    mn = min(nums[l:])
    r = n - 2
    while r >= 0 and nums[r] < nums[r + 1]:
        r -= 1
    mx = max(nums[r::-1])
    i = 0
    while i < n and nums[i] <= mn:
        i += 1    
    j = n - 1
    while j >= 0 and nums[j] >= mx:
        j -= 1
    return j - i + 1 if j - i > 0 else 0


def findUnsortedSubarray_optimal(nums):  # O(n) and O(1)
    ans = 0
    left = len(nums)-1
    max_so_far = float('-inf')
    for i, n in enumerate(nums):
        # if num is new max, update and continue
        if n >= max_so_far:
            max_so_far = n
        # else you need to find the left-most num for which sorting the subarray is sufficient
        else:
            left = min(left, i - 1)
            while left >= 0 and nums[left] > n:
                left -= 1
            ans = i - left
    return ans


def findUnsortedSubarray_stack(nums):  # O(n) and O(1)
    if not nums:
        return 0
    s = [nums[0]]
    failed = False
    for i in range(1, len(nums)):
        if not failed and nums[i] >= s[-1]:
            s.append(nums[i])
            continue
        failed = True
        while s and nums[i] < s[-1]:
            s.pop()
        if not s:
            break
    c = len(s)
    if c == len(nums):
        return 0
    s = [nums[-1]]
    failed = False
    for i in range(len(nums)-2, -1, -1):
        if not failed and nums[i] <= s[-1]:
            s.append(nums[i])
            continue
        failed = True
        while s and nums[i] > s[-1]:
            s.pop()
        if not s:
            break
    return len(nums) - len(s) - c


def findUnsortedSubarray_sorting(nums):  # O(nlogn) and O(n)
    """
    Compare the original list and the sorted list element by element.
    We need to find indices at which mismatches start and end
    """
    nums = list(zip(nums, sorted(nums)))
    num_range = range(len(nums))
    start_idx = next((i for i in num_range if nums[i][0] != nums[i][1]), 0)
    end_idx = next((i for i in reversed(num_range) if nums[i][0] != nums[i][1]), 0)
    return end_idx - start_idx + 1 if start_idx or end_idx else 0


if __name__ == '__main__': 
    print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(findUnsortedSubarray([1, 2, 3, 4]))
    print(findUnsortedSubarray([1]))
    print(findUnsortedSubarray([1, 2, 3, 3, 3]))