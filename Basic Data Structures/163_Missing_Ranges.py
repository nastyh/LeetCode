def findMissingRanges(nums, lower, upper):
    def createRange(s, e):
        return str(s) if s == e else str(s) + "->" + str(e)
    
    nums = [lower - 1] + nums + [upper + 1]
    return [createRange(nums[i-1] + 1, nums[i] - 1)
            for i in range(1, len(nums))
            if nums[i] - nums[i-1] > 1]

def findMissingRanges_alt(nums, lower, upper):
    """
    cover edge cases
    go over the elements. If the element is out of bounds, keep going
    if it's == lower, update the lower
    if it's > lower, if the difference is 1, then we found one missing number
    if the difference is more than one, than here is an interval.
    At the end, cover the last pass manually 
    """
    ans = []
    if not nums:
        if lower == upper:
            return [str(lower)]
        else:
            return [str(lower) + '->' + str(upper)]
        
    for i in range(len(nums)):
        if nums[i] < lower:
            continue
        elif nums[i] == lower:
            lower += 1
        elif nums[i] > lower:
            if lower + 1 == nums[i]:
                ans.append(str(lower))
            else:
                ans.append(str(lower) + '->' + str(nums[i] - 1))
            if nums[i] + 1 <= upper:
                lower = nums[i] + 1
            else:
                return ans
    if nums and nums[-1] < upper:
        if nums[-1] + 1 == upper:
            ans.append(str(upper))
        else:
            ans.append(str(nums[-1] + 1)+'->' + str(upper))
    return ans


def findMissingRanges_another(nums, lower, upper):
    def addRange(self, res, low, high):
    if low + 2 == high:
        res.append(str(low + 1))
    else:
        res.append(str(low + 1) + '->' + str(high - 1))
    
    res = []
    nums = [lower - 1] + nums + [upper + 1]
    for i in range(1, len(nums)):
        curr, prev = nums[i], nums[i - 1]
        if curr - prev > 1:
            addRange(res, prev, curr)
    return res

if __name__ == '__main__':
    print(findMissingRanges([0,1,3,50,75], 0, 99))
    print(findMissingRanges_alt([0,1,3,50,75], 0, 99))