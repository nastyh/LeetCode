from collections import defaultdict
"""
array of integers numbers
count the distinct pairs (i, j) such that 0 <= i < j < len(numbers)
numbers[i], numbrers[j] have the same number of digits
and only one digit differs between the two
"""

def count_distinct_pairs_optimized(numbers):
    """
    O(nd), len of numbers * number of digits
    O(nd), for the hashmap and digit groups 
    precompute masks like *23, 1*3, 12* for each number and store them in a hash map.
    """
    res = 0
    digit_groups = defaultdict(list)
    def _helper(num): # to count digits
        return len(str(abs(num)))

    for num in numbers:
        # dict of the shape {num of digits: numbers from numbers that have this number of digits}
        # say, numbers = [2, 5, 88, 300], then it's {1: [2, 5], 2: [88], 3 : [300]}
        digit_groups[_helper(num)].append(num)

    for group in digit_groups.values():
        mask_map = defaultdict(list)
        for num in group:
            str_num = str(num)
            # Generate all masks for the current number
            for i in range(len(str_num)):
                mask = str_num[:i] + '*' + str_num[i+1:]
                # Count pairs with numbers sharing this mask
                res += len(mask_map[mask])
                # Add this number to the mask_map
                mask_map[mask].append(num)
    return res 
def count_distinct_pairs_basic(numbers):
    """
    O(n + k^2*d), n length of numbers
    k is the size of the largest group, d is the ave num of digits
    O(n) dominates, n length of numbers
    Group numbers by their number of digits in a dict
    For each pair of numbers in the same group, check if they differ by exactly one digit
    Increment res whenever you find a valid pair.
    """
    res = 0
    def _helper(num): # to count digits
        return len(str(abs(num)))
    def _is_diff_by_one(n1, n2):
        str1, str2 = str(n1), str(n2)
        if len(str1) != len(str2): return False 
        diff_count = sum(1 for a, b in zip(str1, str2) if a != b)
        return diff_count == 1
    
    digit_groups = defaultdict(list)
    for num in numbers:
        # dict of the shape {num of digits: numbers from numbers that have this number of digits}
        # say, numbers = [2, 5, 88, 300], then it's {1: [2, 5], 2: [88], 3 : [300]}
        digit_groups[_helper(num)].append(num)

    for group in digit_groups.values():
        n = len(group)
        for i in range(n):
            for j in range(i+1, n):
                if _is_diff_by_one(group[i], group[j]):
                    res += 1
    return res 