from collections import Counter
def findLHS_counter(nums): # O(n) both
    d = Counter(nums)
    res = 0
    for k in d:
        if k + 1 in d:
            res = max(res, d[k] + d[k + 1])
    return res