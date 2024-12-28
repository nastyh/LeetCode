def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
    """
    O(n) for sliding window, constructing the left and right arrays, iterating over middle arrays
    O(n) due to window_sum, left, right arrays
    Use a sliding window to compute sums of all subarrays of length (k) 
    left[i] stores the starting index of the maximum sum subarray from the start up to (i).
    right[i] stores the starting index of the maximum sum subarray from (i) to the end.
    By fixing the middle subarray, the left and right subarrays are determined using left and right arrays. The combined sum of these three subarrays is computed.
    if two sums are equal, the lexicographically smaller indices are chosen.
    """
    n = len(nums)
    # Step 1: Compute the sum of each subarray of size k
    window_sum = [0] * (n - k + 1)
    current_sum = sum(nums[:k])
    window_sum[0] = current_sum
    for i in range(1, len(window_sum)):
        current_sum += nums[i + k - 1] - nums[i - 1]
        window_sum[i] = current_sum
    
    # Step 2: Compute the left maximum indices
    left = [0] * len(window_sum)
    max_idx = 0
    for i in range(len(window_sum)):
        if window_sum[i] > window_sum[max_idx]:
            max_idx = i
        left[i] = max_idx
    
    # Step 3: Compute the right maximum indices
    right = [0] * len(window_sum)
    max_idx = len(window_sum) - 1
    for i in range(len(window_sum) - 1, -1, -1):
        if window_sum[i] >= window_sum[max_idx]:
            max_idx = i
        right[i] = max_idx
    
    # Step 4: Find the three subarrays with the maximum sum
    max_sum = 0
    result = [-1, -1, -1]
    for middle in range(k, len(window_sum) - k):
        l, r = left[middle - k], right[middle + k]
        total = window_sum[l] + window_sum[middle] + window_sum[r]
        if total > max_sum:
            max_sum = total
            result = [l, middle, r]
        elif total == max_sum:
            result = min(result, [l, middle, r])  # Ensure lexicographical order
    
    return result

    def maxSumOfThreeSubarrays_dp(self, nums: List[int], k: int) -> List[int]:
        """
        O(n) both 
        dp1 to store the maximum sum of 1 subarray with length k starting at index i
        dp2 to store the maximum sum of 2 subarray with length k starting at index i
        dp3 to store the maximum sum of 3 subarray with length k starting at index i
        """
        len_n = len(nums)
        # perfix sum list to help calculate the subarray sum
        pf_sum = [0]
        rs = 0
        for n in nums:
            rs += n
            pf_sum.append(rs)
        # dp1 stores the maximum sum of 1 subarray with length k starting at index i
        dp1 = [0] * (len_n - k + 1)
        max_subarr_sum, max_subarr_idx = float('-inf'), None
        subarr_last_idx = len_n
        while subarr_last_idx >= k:
            tsub_sum = pf_sum[subarr_last_idx] - pf_sum[subarr_last_idx - k]
            if tsub_sum >= max_subarr_sum:
                 max_subarr_sum = tsub_sum
                 max_subarr_idx = subarr_last_idx - k
            dp1[subarr_last_idx - k] = (max_subarr_sum, max_subarr_idx)
            subarr_last_idx -= 1
        
        # dp2 stores the maximum sum of 2 subarrays with length k starting at index i
        dp2 = [None] * (len_n - 2 * k + 2)
        dp2[-1] = (0, None)

        subarr_last_idx = len_n - 2 * k
        while subarr_last_idx >= 0:
            two_subarr_sum = pf_sum[subarr_last_idx + k] - pf_sum[subarr_last_idx] + dp1[subarr_last_idx + k][0]
            if two_subarr_sum >= dp2[subarr_last_idx + 1][0]:
                dp2[subarr_last_idx] = (two_subarr_sum, [subarr_last_idx, dp1[subarr_last_idx + k][1]])
            else:
                dp2[subarr_last_idx] = dp2[subarr_last_idx + 1]
            subarr_last_idx -= 1

        # dp3 stores the maximum sum of 3 subarrays with length k starting at index i
        dp3 = [None] * (len_n - 3 * k + 2)
        dp3[-1] = (0, None)

        subarr_last_idx = len_n - 3 * k
        while subarr_last_idx >= 0:
            three_subarr_sum = pf_sum[subarr_last_idx + k] - pf_sum[subarr_last_idx] + dp2[subarr_last_idx + k][0]
            if three_subarr_sum >= dp3[subarr_last_idx + 1][0]:
                dp3[subarr_last_idx] = (three_subarr_sum, [subarr_last_idx, *dp2[subarr_last_idx + k][1]])
            else:
                dp3[subarr_last_idx] = dp3[subarr_last_idx + 1]
            subarr_last_idx -= 1

        return dp3[0][1]


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
