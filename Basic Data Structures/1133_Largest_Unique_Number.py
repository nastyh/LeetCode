import math
from collections import Counter
def largestUniqueNumber(A):  # O(nlogn) and O(n)
    d = Counter(A)
    for key in sorted(d.keys())[::-1]:
        if d[key] == 1:
            return key
        return -1


def largestUniqueNumber_optimal(A):  # O(n) both
    """
    Build a dictionary, go over
    If a value == 1, get the key. But we need the largest, so, update res accordingly
    """
    d = Counter(A)
    res = -math.inf
    for k, v in d.items():
        if v == 1:
            res = max(res, k)
    return res if res != -math.inf else -1


def largestUniqueNumber_short(A):        
        return max([-1] + [k for k,v in collections.Counter(A).items() if v == 1])