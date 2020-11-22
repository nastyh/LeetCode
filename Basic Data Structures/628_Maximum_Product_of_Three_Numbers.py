import math
def maximumProduct(nums):  # sorting O(nlogn) in time and O(nlogn) in space 
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


def maximumProduct_scan(nums):  # O(n) and O(1)
    min1, min2 = math.inf, math.inf
    max1, max2, max3 = -math.inf, -math.inf, -math.inf
    for num in nums:
        if num <= min1:
            min2 = min1
            min1 = num
        elif num <= min2:
            min2 = num
        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = n 
        elif num >= max3:
            max3 = num
    return max(min1 * min2 * max1, max1 * max2 * max3)

if __name__ == '__main__':
    print(maximumProduct([1, 2, 3]))
    print(maximumProduct([1, 2, 3, 4]))
    print(maximumProduct([-4, -3, -2, -1, 60]))
    print(maximumProduct_scan([1, 2, 3]))
    print(maximumProduct_scan([1, 2, 3, 4]))
    print(maximumProduct_scan([-4, -3, -2, -1, 60]))
    