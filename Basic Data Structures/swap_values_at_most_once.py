"""
You are given an array of N elements. This array represents the digits of a number. In an operation, you can swap the value at any two indices. Your task is to find the maximum number by using operation at most once.
For Example :
Input array [1,3,2,7] so basically this array represents the number 1327.
All the possible combinations are :
1. [3 1 2 7] get by swapping indices 1 and 2.
2. [2 3 1 7] get by swapping indices 1 and 3.
3. [7 3 2 1] get by swapping indices 1 and 4.
4. [1 2 3 7] get by swapping indices  2 and 3.
5. [1 7 2 3] get by swapping indices 2 and 4.
6. [1 3 7 2] get by swapping indices 3 and 4.
Out of all the possible combinations, 3 give the maximum number as 7321, so we will return [7 3 2 1].
"""
def maximum_swap(arr):
    """
    O(n) to iterate
    O(1) for dict that has at most 10 digits
    The dictionary last_index holds the last occurrence of each digit.
    This ensures that when we want to swap, we get the rightmost (and thus the most impactful) occurrence of a larger digit.
    For each digit at position i, we check for any digit d from 9 down to arr[i] + 1.
    If d is found later in the array (i.e., its recorded index is greater than i),
    we perform the swap and return immediately because only one swap is allowed.
    """
    n = len(arr)
    # Record the last position of each digit (0-9)
    last_index = {x: i for i, x in enumerate(arr)}
    
    for i in range(n):
        # Check digits larger than the current one, from 9 down to arr[i]+1
        for d in range(9, arr[i], -1):
            if last_index.get(d, -1) > i:
                # Swap and return immediately as we can only do one swap.
                arr[i], arr[last_index[d]] = arr[last_index[d]], arr[i]
                return arr
    return arr
