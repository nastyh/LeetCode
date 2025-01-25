"""
Given an integer n and an array a of length n, your task is to apply the following mutation to a:
    Array a mutates into a new array b of length n. For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
    If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0.
    For example, b[0] should be equal to 0 + a[0] + a1.
"""
def mutate_array_clean(n, a):
    """
    O(n) both 
    create res of the same size
    start with the second element and go to the second last element 
    and just fill it out
    take care of the first and last elements manually 
    return res 
    """
    res = [0] * len(a)
    if len(a) == 0: return []
    if len(a) == 1: return [a[0]]
    for ix in range(1, len(a) - 1):
        left_val = a[ix-1]
        middle_val = a[ix]
        right_val = a[ix+1]
        res[ix] = left_val + middle_val + right_val
    res[0] = a[0] + a[1]
    res[-1] = a[-1] + a[-2]
    return res 
def mutate_array(n, a):
    """
    O(n) to iterate over the list a of length n 
    O(n) to create a new list b of size n
    For each index i in a
    Check if i - 1 is valid; if not, use 0.
    Check if i + 1 is valid; if not, use 0.
    Calculate b[i] as the sum of these values.
    """
    # Initialize the resulting array
    b = [0] * n
    # Calculate each element in b
    for i in range(n):
        left = a[i - 1] if i - 1 >= 0 else 0
        middle = a[i]
        right = a[i + 1] if i + 1 < n else 0
        b[i] = left + middle + right
    return b
