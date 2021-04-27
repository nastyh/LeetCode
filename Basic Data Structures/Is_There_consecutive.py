"""
takes nums, n, times
Return True if the number n is in nums exactly times times in a row.
False otherwise
"""
from collections import Counter
def is_there_consetuve(nums, n, times):
    res = 0
    for num in nums:
        if num == n:
            res += 1
        elif nums != n:
            if res != times:
                res = 0 
    return res == times
        

if __name__ == '__main__':
    print(is_there_consetuve([1, 3, 5, 5, 3, 3, 1], 3, 2))  # True
    print(is_there_consetuve([1, 2, 3, 4, 5], 1, 1))  # True
    print(is_there_consetuve([3], 1, 0))  # True
    print(is_there_consetuve([2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5], 3, 2))  # False b/c there are no two 3s in a row
    print(is_there_consetuve([5, 5, 5, 5, 5], 5, 7))  # False 