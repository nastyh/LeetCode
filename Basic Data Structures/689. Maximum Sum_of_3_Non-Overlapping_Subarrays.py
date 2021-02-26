def maxSumOfThreeSubarrays(nums, k):  # O(n) both 
    """
    create a new siliding_window[i], and use the results from our previous iterations to track the maximum value behind it.
    In this way, we can create generations of optimal results for a growing number of windows.
    The process can be initialized with an empty array of zeros (nothing found behind the first window).
    At every step, we discard any results that didn't create a new maximum (and copy our old values instead).
    """
    def _helper(nums, k):
        s = sum(nums[:k])
        S = [s]
        for i in range(k,len(nums)):
            s += nums[i] - nums[i - k]
            S.append(s)
        return S
    L = len(nums)
    if (k * m) >= L:
        return sum(nums)
    S    = _helper(nums, k)
    Aprev = [ [0,[]] for _ in range(L) ]
    for i in range(m):
        Anew  = [ [ Aprev[0][0] + S[i * k], Aprev[0][1] + [i * k] ] ]
        for j in range(i * k + 1,len(S)):
            sp,ip = Aprev[j - i * k]
            s = S[j] + sp
            if s>Anew[-1][0]:
                Anew.append( [s, ip + [j]])
            else:
                Anew.append(Anew[-1])
        Aprev = Anew
    return Anew[-1][-1]


def maxSumOfThreeSubarrays_brute_force(nums, k): # O(n^3)
    maxS = float('-inf')
    res = []
    # e1, e2, e3 are ending indices of first, second and third intervals.
    for e1 in range(k - 1, N - 2 * k):
        s1 = e1 - k + 1
        for e2 in range(e1 + k, N - k):
            s2 = e2 - k + 1
            for e3 in range(e2 + k, N):
                s3 = e3 - k + 1
                tsum = dp[e1] + dp[e2] + dp[e3] 
                if tsum > maxS:
                    maxS = tsum
                    res = [s1, s2, s3]
    return res