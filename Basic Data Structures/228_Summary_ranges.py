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


def summaryRanges_another(nums):
    """
    Has a bunch of annoying edge cases that are at the end of the code
    First, get out simple edge cases
    Then put the first element into curr and start traversing through the rest of nums
    If nums[i] is 1 larger than the last element in curr, then append nums[i]
    If it's not a case, then we need to prepare an interval for res
    If len(curr) > 1, it means there is an interval there. Add it to res with all the required symbols. Clean and update curr after it
    If len(curr) == 1, it means there is a single number there. Add only this number. Clean and update curr after it
    Once we get to the end of nums (i == len(nums) - 1), we need to make the last addition.
    If there is only one element in curr, add it. If there are more, add an interval 
    """
    if len(nums) == 0: return []
    if len(nums) == 1: return [str(nums[0])]
    res = []
    curr = []
    curr.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i] - curr[-1] == 1:
            curr.append(nums[i])
        else:
            if len(curr) > 1:
                res.append(str(curr[0]) + '->' + str(curr[-1]))
                curr = []
                curr.append(nums[i])
            else:
                res.append(str(curr[-1]))
                curr = []
                curr.append(nums[i])
        if i == len(nums) - 1 and len(curr) == 1:
            res.append(str(nums[-1]))
        if i == len(nums) - 1 and len(curr) > 1:
            res.append(str(curr[0]) + '->' + str(curr[-1]))
    return res

if __name__ == '__main__':
    print(summaryRanges([0,2,3,4,6,8,9]))
    print(summaryRanges_alt([0,2,3,4,6,8,9]))
    print(summaryRanges_indices([0,2,3,4,6,8,9]))
    print(summaryRanges_another([0,2,3,4,6,8,9]))