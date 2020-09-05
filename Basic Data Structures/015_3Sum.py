def threeSum(nums):
    l = len(nums)
    nums.sort()
    ans = set()
    for i in range(0,l-2):
        d = set()
        s = 0-nums[i]

        for j in range(i+1,l):
            x = s-nums[j]
            if x not in d:
                d.add(nums[j])
            else:
                ans.add((nums[i],nums[j],x))
    return list(ans)


def Sum3_with_helper(nums): # with pointers, easier to comprehend
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


# def test(array, target):
#     l, r = 0, len(array) - 1
#     res, curr = [], []
#     while l < r:
#         if array[l] + array[r] == target:
#             curr = []
#             curr.append(array[l])
#             curr.append(array[r])
#             curr.append(target)
#             l += 1
#             r -= 1
#             # res.append(target)
#             # return res
#         elif array[l] + array[r] < target:
#             l += 1
#         else:
#             r -= 1
#         if len(curr) > 0: res.append(curr)
#     return res if len(res) > 0 else []
if __name__ == '__main__':
    # print(threeSum_pointers([-1, 0, 1, 2, -1, -4]))
    # print(threeSum_pointers([0,0,0,0]))
    # print(threeSum_pointers([-2,0,1,1,2]))
    # print(test([0, 1, 2, -1, -4], 1))
    # print(threeSum([-1, 0, 1, 2, -1, -4]))
    # print(test([-4, -1, 0, 1, 2], 1))
    # print(test([-4, -1, -1, 1, 2], 0))
    # print(test([-4, -1, -1, 0, 2], -1))
    # print(test([0, 1, 1, 2], 2))
    print(Sum3_with_helper([-1, 0, 1, 2, -1, -4]))