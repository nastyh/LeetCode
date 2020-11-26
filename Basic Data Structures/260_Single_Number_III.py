from collections import Counter
def singleNumber(nums):  # easiest but extra space
    d = Counter(nums)
    return [k for k,v in d.items() if v== 1]


def singleNumber_efficient(nums):
    # difference between two numbers (x and y) which were seen only once
    bitmask = 0
    for num in nums:
        bitmask ^= num
    
    # rightmost 1-bit diff between x and y
    diff = bitmask & (-bitmask)
    
    x = 0
    for num in nums:
        # bitmask which will contain only x
        if num & diff:
            x ^= num
    
    return [x, bitmask^x]


if __name__ == '__main__':
    print(singleNumber([1, 2, 1, 3, 2, 5]))
    print(singleNumber_efficient([1, 2, 1, 3, 2, 5]))

