def wiggleMaxLength_iter(nums):  # O(n) and O(1)
    n = len( nums )
    # length of wiggle sequence, ending in positive difference, negative difference
    positive, negative = 1, 1
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            # difference is positive, concatenated with negative prefix wiggle subsequence
            positive = negative + 1
        elif nums[i] < nums[i - 1]:
            # differnce is negative, concatenated with positive prefix wiggle subsequence
            negative = positive + 1
    # compute the longest length of wiggle sequence                
    return max(positive, negative)


def wiggleMaxLength_dp(nums):  # O(n^2) and O(n)
    if not nums:
        return 0
    less = [1] * len(nums)
    more = [1] * len(nums)
    res_l = 1
    res_m = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and more[i] < less[j] + 1:
                more[i] = less[j] + 1
                res_m = more[i]
            elif nums[i] < nums[j] and less[i] < more[j] + 1:
                less[i] = more[j] + 1
                res_l = less[i]
    return max(res_l,res_m)