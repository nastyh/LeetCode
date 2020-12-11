def nextGreaterElements(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [-1]
    res = [-1] * len(nums)
    for i in range(len(nums)):
        for j in nums[i + 1:] + nums[:i]:
            if j > nums[i]:
                res[i] = j
    return res


def nextGreaterElements_stack(nums):
    stack, res, n = [], [-1]*len(nums), len(nums)
    for i in range(0, 2 * n):
        while stack and nums[i % n] > nums[stack[-1]]:
            top = stack.pop()
            if res[top] == -1:
                res[top] = nums[i % n]
        stack.append(i % n)
    return res


if __name__ == '__main__':
    print(nextGreaterElements([1, 2, 1]))
    print(nextGreaterElements([1, 2, 3, 4, 3]))  # fails for some reason
    print(nextGreaterElements_stack([1, 2, 1]))
    print(nextGreaterElements_stack([1, 2, 3, 4, 3]))