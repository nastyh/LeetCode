def summaryRanges(nums):
    if not nums:
        return []
    stack = []
    i = 0
    res = []
    while i < len(nums):
        if stack and nums[i] - stack[-1] != 1:
            if len(stack)==1:
                res.append(str(stack[-1]))
            else:
                res.append(str(stack[0]) + '->' + str(stack[-1]))

            while stack:
                stack.pop()

        stack.append(nums[i])
        i+=1
    if len(stack)==1:
        res.append(str(stack[-1]))
    else:
        res.append(str(stack[0]) + '->' + str(stack[-1]))
    return res

def summaryRanges_alt(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [str(nums[0])]
    res = []
    start = nums[0]
    prev = nums[0]
    for n in nums[1:]:
        if n != prev + 1:
            if prev == start:
                res.append(str(start))
            else:
                res.append(str(start) + '->' + str(prev))
            start = n
        prev = n
    if prev == start:
        res.append(str(start))
    else:
        res.append(str(start) + '->' + str(prev))
    return res

def summaryRanges_indices(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [str(nums[0])]
    l, r, res = 0, 0, []
    for ix in range(1, len(nums)):
        if nums[ix] != nums[r] + 1:
            if nums[r] == nums[l]:
                res.append(str(nums[l]))
            else:
                res.append(str(nums[l]) + '->' + str(nums[r]))
            l = ix
        r = ix
    if nums[r] == nums[l]:
        res.append(str(nums[l]))
    else:
        res.append(str(nums[l]) + '->' + str(nums[r]))
    return res

if __name__ == '__main__':
    print(summaryRanges([0,2,3,4,6,8,9]))
    print(summaryRanges_alt([0,2,3,4,6,8,9]))
    print(summaryRanges_indices([0,2,3,4,6,8,9]))