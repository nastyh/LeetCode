def largestAltitude(gain):  # O(n) and O(1)
    """
    Just build a running sum in curr_res and update res
    """
    res = 0
    curr_res = 0
    for num in gain:
        curr_res += num
        res = max(res, curr_res)
    return res