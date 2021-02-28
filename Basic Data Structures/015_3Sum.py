def threeSum(nums):  # O(n^2) and O(n)
    l = len(nums)
    nums.sort()
    ans = set()
    for i in range(0, l - 2):
        d = set()
        s = 0 - nums[i]
        for j in range(i + 1, l):
            x = s - nums[j]
            if x not in d:
                d.add(nums[j])
            else:
                ans.add((nums[i], nums[j], x))
    return list(ans)


def Sum3_with_helper(nums): # with pointers, easier to comprehend  O(nlogn) and O(n)
    nums.sort()
    res = []
    def _helper(array, ix, res):
        l, r = ix + 1, len(array) - 1
        while l < r:
            temp = nums[ix] + nums[l] + nums[r]
            if temp < 0 or (l > ix + 1 and nums[l] == nums[l - 1]):
                l += 1
            elif temp > 0 or (r < len(nums) - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                res.append([nums[ix], nums[l], nums[r]])
                l += 1
                r -= 1
    for ix in range(len(nums)):
        if nums[ix] > 0:
            break
        if ix == 0 or nums [ix - 1] != nums[ix]:
            _helper(nums, ix, res)
    return res


def threeSum_sorting(nums):  # O(n^2 + nlogn) and O(n)
    """
    Solution with sorting (nlogn(n))
    For every element do two sum on the elements to the right from a current element
    Two extra edge cases here:
    don't want to redo for the same elements. Taken care of by if k > 0 and nums[k] == nums[k - 1]:
    Another edge case is [-2, 0, 0, 2, 2]. Once we found [2, 0, -2], we move left and right inwards and end up with another [2, 0, -2]
    To avoid it, we have two while loops after we found a triplet 
    """
    res = []
    nums.sort()
    def _helper(numbers, target):
        nonlocal res
        l, r = 0, len(numbers) - 1
        while l < r: 
            if numbers[l] + numbers[r] == target:
                res.append([-target, numbers[l], numbers[r]])
                l += 1
                r -= 1
                while l < r and numbers[l] == numbers[l - 1]:
                    l += 1
                while l < r and numbers[r] == numbers[r + 1]:
                    r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
    for k, v in enumerate(nums):
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        _helper(nums[k + 1:], -v)
    return res



if __name__ == '__main__':
    # print(threeSum_pointers([-1, 0, 1, 2, -1, -4]))
    # print(threeSum_pointers([0,0,0,0]))
    # print(threeSum_pointers([-2,0,1,1,2]))
    # print(threeSum([-1, 0, 1, 2, -1, -4]))
    # print(Sum3_with_helper([-1, 0, 1, 2, -1, -4]))
    print(threeSum_sorting([-1, 0, 1, 2, -1, -4]))
    print(threeSum_sorting([-2, 0, 0, 2, 2]))
    print(threeSum_sorting([0, 0, 0, 0]))
