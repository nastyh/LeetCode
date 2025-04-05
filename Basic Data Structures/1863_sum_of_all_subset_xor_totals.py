def subsetXORSum(nums):
    # Calculate the bitwise OR of all numbers
    bitwise_or = 0
    for num in nums:
        bitwise_or |= num

    # Multiply the bitwise OR with 2^(n-1)
    return bitwise_or * (2 ** (len(nums) - 1))