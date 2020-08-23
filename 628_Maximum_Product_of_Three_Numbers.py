import heapq
def maximumProduct(nums):  # sorting
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

if __name__ == '__main__':
    print(maximumProduct([1, 2, 3]))
    print(maximumProduct([1, 2, 3, 4]))
    print(maximumProduct([-4, -3, -2, -1, 60]))
    