from collections import Counter
def minIncrementForUnique(A):  # O(n) both
    if not A:
        return 0
    diff = 0
    stack = []
    c = Counter(A)
    for i in range(min(c.keys()), max(c.keys())+1):
        if i in c:
            stack += [i] * (c[i] - 1)
        elif i not in c and stack:
            diff += i - stack.pop()
    return diff + sum(range(i+1, i+1+len(stack))) - sum(stack)


def minIncrementForUnique_sort(A):  # O(nlogn) and O(1)
    A.sort()
    nextNum = float('-inf')
    steps = 0
    for num in A:
        steps += max(nextNum, num) - num
        nextNum = max(num, nextNum) + 1
    return steps


def minIncrementForUnique(arr):   # O(nlogn) and O(1)
    """
    first sort the array, and store its sum
    then create new array by incrementing each duplicate element with maximum value of itself + 1 and previous element. do this in place
    store the sum of newly created array
    the difference between the two sums is the total number of incrementes made
    before arr = [1, 1, 1, 1, 3, 5], sum1 = 12
    after arr = [1, 2, 3, 4, 5, 6] sum2 = 21
    total moves = 21 - 12 = 9

    """
    arr.sort()
    s1 = sum(arr)
    n = len(arr)
    for i in range(1, n): 
        if arr[i] <= arr[i - 1]:
            arr[i] = max(arr[i], arr[i - 1] + 1)
    s2 = sum(arr)
    return s2 - s1