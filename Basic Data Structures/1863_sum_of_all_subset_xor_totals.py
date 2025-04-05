def subsetXORSum(nums):
    """
    O(n) to iterate once
    O(1) nothing to store
    the sum of the XOR totals for all subsets of an array is equal to the bitwise OR of all the elements multiplied by
    2^(n-1), where n is the num of the elements in nums
    For any subset, the XOR operation will include that bit if and only if an odd number of the elements in that subset have the bit set.
    A bit that is set in at least one element will eventually contribute to the XOR total of many subsets.
    It turns out that for every bit, if you take the bitwise OR of all numbers, then this OR will have that bit set if it appears in any number.
    This single bit will contribute 2^(n-1) times in sthe sum over all subsets
    
    If B is the bitwise OR of all elements in the array, the total sum is B * 2^(n-1)
    """
    # Calculate the bitwise OR of all numbers
    bitwise_or = 0
    for num in nums:
        bitwise_or |= num

    # Multiply the bitwise OR with 2^(n-1)
    return bitwise_or * (2 ** (len(nums) - 1))

def subsetXORSum_helpers(nums):
    """
    O(n*2^n): 2^n subsets for a list of length n. Generating each takes up to O(n)
    O(n*2^n), each subset might take up to O(n) and we have 2^n of such subsets 

    XOR func 
    is O(n*2^n) and O(1)

    More straigthforward. 
    First helper takes a list and calculates the overall XOR output for a given list
    0 ^ number = number, that's why res = 0 originally

    Second helper creates a list of lists of all possible subsets (with repetitions per task)

    Get a list of subsets and hit it with the first helper.
    Return glob_res
    """
    glob_res = 0

    def _xor_list(arr):
        res = 0
        for n in arr:
            res ^= n
        return res
    def _subsets(nums):
        all_subsets = []
        def _backtrack(ix, curr):
            all_subsets.append(curr[:])
            for i in range(ix, len(nums)):
                curr.append(nums[i])
                _backtrack(i+1, curr)
                curr.pop()
        _backtrack(0, [])
        return all_subsets 
    for subset in _subsets(nums):
        glob_res += _xor_list(subset)
    return glob_res 
