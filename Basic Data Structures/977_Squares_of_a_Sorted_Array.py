import heapq
def sortedSquares_best_shortest(nums):  # O(n) both (if we count res)
    """
    Cover edge cases 
    We will fill out res from right to left b/c the most right number is the largest
    It will be filled out by either the most left or the most right number from nums.
    Have three pointers, l, r, and i. 
    Compare the absolute values at the left and right ends of nums. Take the higher, plant into res[i]
    Move indices accordingly 
    """
    if len(nums) == 0: return
    if len(nums) == 1: return [x**2 for x in nums]
    if all([x >= 0 for x in nums]): return  [x**2 for x in nums]
    l, r, i, res = 0, len(nums) - 1, len(nums) - 1, [None] * len(nums)
    while l <= r:
        if abs(nums[l]) >= abs(nums[r]):
            res[i] = nums[l]**2
            l += 1
            i -= 1
        else:
            res[i] = nums[r]**2
            r -= 1
            i -= 1
    return res



def sortedSquares(nums): # pythonic  O(nlogn) and O(N)
    return sorted([i**2 for i in nums])


def sortedSquares_list(nums):  # O(N) both
    """
    Fill out from the end: from the largest element
    """
    res = [None] * len(nums)
    l, r = 0, len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[l]) > abs(nums[r]):
            res[i] = nums[l]**2
            l += 1
        else:
            res[i] = nums[r]**2
            r -= 1
    return res
    
def sortedSquares_heap(nums): 
    h = []
    res = [0] * len(nums)
    for num in nums:
        h.append(abs(num))
    heapq.heapify(h)
    ix = 0
    while len(h) > 0:
        curr = heapq.heappop(h)
        res[ix] = curr*curr
        ix += 1
    return res


def sortedSquares_efficient(nums):  # O(N) both
    if len(nums) == 0: return
    if len(nums) == 1: return [x**2 for x in nums]
    if all([x >= 0 for x in nums]): return  [x**2 for x in nums]
    if all([x < 0 for x in nums]): return  [x**2 for x in nums][::-1]
    l, r, res = 0, len(nums) - 1, []

    while nums[l] < 0: # finding the index of the most right element that is < 0
        l += 1
    l -= 1  # stepping back b/c we overshoot
    while nums[r] >= 0: # finding the index of the most left element that is > 0
        r -= 1
    r += 1  # stepping back b/c we overshoot

    while l >= 0 and r < len(nums): # moving l to the left and r to the right
        if abs(nums[l]) <= abs(nums[r]):
            res.append(nums[l]**2)
            l -= 1
        else:
           res.append(nums[r]**2)
           r += 1
    while l >= 0: # because we might start not in the middle of the list, we can have elements left on one of the sides
        res.append(nums[l]**2)
        l -= 1
    while r < len(nums):
        res.append(nums[r]**2)
        r += 1

    # if l != 0:
    #     res.extend([i**2 for i in list(reversed(nums[:l + 1]))])
    # if r != len(nums) - 1:
    #     res.extend([i**2 for i in nums[r:]])
    # return nums[l], nums[r]
    # return l, r
    return res


def sortedSquares_alt(nums): 
    """
    Cover edge cases
    Create two lists: left_nums are squared nums up to zero. Result is decreasing
    right_nums are squared numbers from the right from zero but they're in a decreasing order
    Reverse both, start comparing and appending
    Keep care of a situation when one list is longer than another
    """
    res = []
    if len(nums) == 1: return [nums[0]**2]
    if all(i >= 0 for i in nums): return [i**2 for i in nums]
    if all(i < 0 for i in nums): return [i**2 for i in nums][::-1]
    left_nums, right_nums = [], []
    i = 0
    while i < len(nums) and nums[i] <= 0:  # the order is important, won't work with [-2, 0] otherwise 
        left_nums.append(nums[i]**2)
        i += 1
    j = len(nums) - 1
    while nums[j] > 0:
        right_nums.append(nums[j]**2)
        j -= 1
    left_nums_rev, right_nums_rev = left_nums[::-1], right_nums[::-1]
    if len(left_nums_rev) == 0 and len(right_nums_rev) != 0:
        return right_nums_rev
    if len(left_nums_rev) != 0 and len(right_nums_rev) == 0:
        return left_nums_rev
    l, r = 0, 0
    while l < len(left_nums_rev) and r < len(right_nums_rev):
        if left_nums_rev[l] <= right_nums_rev[r]:
            res.append(left_nums_rev[l])
            l += 1
        else:
            res.append(right_nums_rev[r])
            r += 1
    if l != len(left_nums_rev):
        res.extend([i for i in left_nums_rev[l:]])
    if r != len(right_nums_rev):
        res.extend([j for j in right_nums_rev[r:]])
    return res


if __name__ == '__main__':
    # print(sortedSquares([-4, -1, 0, 3, 10]))
    # print(sortedSquares([-7, -3, 2, 3, 11]))
    # print(sortedSquares_efficient([-4,-1, 0, 3, 10]))
    # print(sortedSquares_efficient([-7,-3, 2, 3, 11]))
    # print(sortedSquares_alt([-4,-1, 0, 3, 10]))
    # print(sortedSquares_alt([-7,-3, 2, 3, 11]))
    # print(sortedSquares_efficient([-2, 0]))
    print(sortedSquares_alt([-2, 0]))
    print(sortedSquares_alt([-5, -3, -2, -1]))
    print(sortedSquares_efficient([-5, -3, -2, -1]))
    print(sortedSquares_efficient([-2, 0]))

