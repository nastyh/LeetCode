def maxEnvelopes(envelopes):
    if len(envelopes) <= 1: return len(envelopes)
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    res, curr = 0, envelopes[0]
    for ix in range(1, len(envelopes)):
        if curr[0] < envelopes[ix][0] and curr[1] < envelopes[ix][1]:
            res += 1
            curr = envelopes[ix]
    return res + 1


def maxEnvelopes_dp(envelopes):
    if len(envelopes) <= 1: return len(envelopes)
    envelopes.sort(key = lambda x: (x[0], -x[1]))
    size = 0
    dp = [0] * len(envelopes)
    for _, h in envelopes:
        l, r = 0, size - 1
        while l <= r:
            mid = (l+r) // 2
            if dp[mid] >= h:
                r = mid - 1
            else:
                l = mid + 1  
        dp[l] = h
        size = max(size, l + 1)
    return size


if __name__ == '__main__':
    print(maxEnvelopes([[5, 4],[6, 4],[6, 7],[2, 3]]))
    print(maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500],[5, 400], [5, 250], [6, 370],[6, 360], [7, 380]])) # doesn't pass this case for some reason
    print(maxEnvelopes_dp([[5, 4],[6, 4],[6, 7],[2, 3]]))
    print(maxEnvelopes_dp([[2, 100], [3, 200], [4, 300], [5, 500],[5, 400], [5, 250], [6, 370],[6, 360], [7, 380]]))
        