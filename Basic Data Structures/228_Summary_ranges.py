def summaryRanges(nums):
    if not nums:
        return []

    stack = []

    i = 0
    res = []
    while i < len(nums):

        if stack and nums[i] -stack[-1] !=1:
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


if __name__ == '__main__':
    print(summaryRanges([0,2,3,4,6,8,9]))
