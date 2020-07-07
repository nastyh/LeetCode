def sortedSquares(nums): # pythonic
    return sorted([i**2 for i in nums])

def sortedSquares_efficient(nums):
    if len(nums) == 0: return
    if len(nums) == 1: return [x**2 for x in nums]
    if all([x >=0 for x in nums]): return  [x**2 for x in nums]
    l, r, res = 0, len(nums) - 1, []

    while nums[l] < 0: # finding the index of the most right element that is < 0
        l += 1
    l -= 1
    while nums[r] >= 0: # finding the index of the most left element that is > 0
        r -= 1
    r += 1

    while l >= 0 and r < len(nums): # moving l to the left and r to the right
        if abs(nums[l]) <= abs(nums[r]):
            res.append(nums[l]**2)
            l -= 1
        else:
           res.append(nums[r]**2)
           r += 1

    while l >=0: # because we might start not in the middle of the list, we can have elements left on one of the sides
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


if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))
    # print(sortedSquares([-7,-3,2,3,11]))
    print(sortedSquares_efficient([-4,-1,0,3,10]))
    print(sortedSquares_efficient([-7,-3,2,3,11]))
