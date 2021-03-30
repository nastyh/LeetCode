def maxEnvelopes_dp(envelopes):  # O(nlogn) and O(n)
    """
    We want to perform a longest increasing subsequence exercise on the second dimension
    """
    if len(envelopes) <= 1: return len(envelopes)
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    size = 0
    dp = [0] * len(envelopes)
    for _, h in envelopes:
        l, r = 0, size - 1
        while l <= r:
            mid = (l + r) // 2
            if dp[mid] >= h:
                r = mid - 1
            else:
                l = mid + 1  
        dp[l] = h
        size = max(size, l + 1)
    return size


if __name__ == '__main__':
    print(maxEnvelopes_dp([[5, 4],[6, 4],[6, 7],[2, 3]]))
    print(maxEnvelopes_dp([[2, 100], [3, 200], [4, 300], [5, 500],[5, 400], [5, 250], [6, 370],[6, 360], [7, 380]]))
        