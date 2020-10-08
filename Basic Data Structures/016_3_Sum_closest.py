import math
def threeSumClosest(nums, target):
    diff = math.inf
    nums.sort()
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            temp = nums[i] + nums[l] + nums[r]
            if abs(target - temp) < abs(diff):
                diff = target - temp
            if temp < target:
                l += 1
            else:
                r -= 1
        if diff == 0:
            break
    return target - diff


if __name__ == '__main__':
    print(threeSumClosest([-1,2,1,-4], 1))
    print(threeSumClosest_alt([-1,2,1,-4], 1))
