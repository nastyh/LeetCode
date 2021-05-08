from collections import Counter
def frequencySort(nums):  # O(nlogn) and O(n)
    """
    Key here is to sort based on two parameters: x[1] and -x[0]. 
    First sort in the increasing order by value
    Then, if there is a tie, sort in the decreasing order by key
    Extend() adds each key the value number of times to res 
    """
    res, d = [], Counter(nums)
    for k, v in sorted(d.items(), key = lambda x: (x[1], -x[0])):
        res.extend(k for _ in range(v))
    return res
        