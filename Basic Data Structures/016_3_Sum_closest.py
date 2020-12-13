import math
def threeSumClosest(nums, target):  # O(nlogn + n^2) --> O(n^2)
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


def threeSumClosest_alt(nums, target):
    if not nums:
        return None
    diff = math.inf
    nums.sort()
    for i in range(len(nums) - 2):
        p1=i + 1
        p2=len(nums) - 1
        while p1 < p2:
            s=nums[i] + nums[p1] + nums[p2]
            if abs(s - target) < diff:
                diff = abs(s - target)
                output = s
            
            if s < target:
                p1 += 1
            elif s > target:
                p2 -= 1
            else:
                return target
    return output       

if __name__ == '__main__':
    print(threeSumClosest([-1, 2, 1, -4], 1))
    print(threeSumClosest_alt([-1, 2, 1 , -4], 1))
