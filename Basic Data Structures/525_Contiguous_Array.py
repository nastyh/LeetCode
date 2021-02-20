def findMaxLength_another(nums):  # O(n) both
    """
    Go through nums.
    If a num is zero, decrement curr_count, else increment.
    When curr_count becomes 0, it means that we have a subsequence with the same number of 1s and 0s.
    We will also have a dictionary that will contain {curr_count: at which index we arrived to this count, basically, it's the length of the subsequence}
    If we come across a situation when we've already seen this curr_count (it's in the dictionary already),
    we'll choose the max between the current index (length of the current subsequence) and the previous result in res.
    """
    d = {0: -1}
    res, curr_count = 0, 0
    for i in range(len(nums)):
        if nums[i] == 0:
            curr_count -= 1
        else:
            curr_count += 1
        if curr_count in d:
            res = max(res,  i - d[curr_count])
        else:
            d[curr_count] = i
    return res
