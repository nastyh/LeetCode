def findDisappearedNumbers(nums):
        # first solution
        # s = set(nums)
        # return [i for i in range(1,len(nums)+1) if i not in s]=
        # second solution
        d = dict(zip(range(1, len(nums)+1),[0]*len(nums)))
        for num in nums:
            if num in d:
                d[num] +=1
        return [k for (k,v) in d.items() if v==0]

def findDisappearedNumbers_fast(nums):
    return [k for k, v in enumerate(nums, 1) if k not in nums]


def findDisappearedNumbers_constant_space(nums):  # O(n) and O(1)
    """
    Need to go over the list and make numbers negative. 
    Then go over the ideal list and check if any of such numbers in the original list are > 0. 
    If so, we haven't seen such a number in nums, then add to res 
    """
    res = []
    for k, v in enumerate(nums):
        if nums[abs(v) - 1] >= 0:
            nums[abs(v) - 1] *= -1
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            res.append(i)
    return res


if __name__ == '__main__':
    # print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
    print(findDisappearedNumbers_fast([4, 3, 2, 7, 8, 2, 3, 1]))
    print(findDisappearedNumbers_constant_space([4, 3, 2, 7, 8, 2, 3, 1]))
