def threeSumSmaller(nums, target):
    nums.sort()
    res = 0

    def _helper(arr, l, target):
        s, r = 0, len(arr) - 1
        while l < r:
            if arr[l] + arr[r] < target:
                s += r - l
                l += 1
            else:
                r -= 1
        return s

    for i in range(len(nums) - 2):
        res += _helper(nums, i + 1, target - nums[i])
    return res

def threeSumSmaller_alt(nums, target):
    result = 0
    nums.sort()
    for i in range(len(nums) - 2):
      l, r = i + 1, len(nums) - 1
      while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < target:
          result += r - l
          l += 1
        else:
          r -= 1
    return result

if __name__ == '__main__':
    print(threeSumSmaller([-2,0,1,3], 2))
    print(threeSumSmaller_alt([-2,0,1,3], 2))
