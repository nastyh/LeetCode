from collections import defaultdict
def countRangeSum(nums, lower, upper):  # O(n) both
    """
    nums = [1,3,4]
    cumsum = [0,1,4,8]
    cumcum[1] means nums[:1]'s prefix sums
    count those where cumsum[j] - cumsum[i] is in [lower,upper].
    """
    cumsum = [0]
    for n in nums:
        cumsum.append(cumsum[-1] + n)
    record = defaultdict(int)
    res = 0
    for csum in cumsum:
        for target in range(lower,upper + 1):
            if csum - target in record:
                res += record[csum - target]
        record[csum] +=1
    return res


def countRangeSum_merge_sort(nums, lower, upper):  # O(n) both 
    cumsum = [0]
    for n in nums:
        cumsum.append(cumsum[-1] + n)
    # inclusive
    def mergesort(l,r):
        if l == r:
            return 0
        mid = (l + r) // 2
        cnt = mergesort(l,mid) + mergesort(mid + 1, r)
        i = j = mid + 1
        # O(n)
        for left in cumsum[l:mid+1]:
            while i <= r and cumsum[i] - left < lower:
                i += 1
            while j <= r and cumsum[j] - left <= upper:
                j+=1
            cnt += j - i
        cumsum[l:r+1] = sorted(cumsum[l:r + 1])
        return cnt
        
    return mergesort(0, len(cumsum) - 1)