from collections import defaultdict
def subarraysDivByK_optimal(A, K):  # O(n) both 
    freq = defaultdict(int, {0: 1})
    ans = prefix = 0
    for x in A: 
        prefix = (prefix + x) % K 
        ans += freq[prefix]
        freq[prefix] += 1
    return ans 



def subarraysDivByK(A, K):  # doesn't work for some cases
    l, r = 0, 0 
    res = 0
    curr_sum = 0
    while r < len(A):
        curr_sum += A[r]
        # print("Before subtracting", curr_sum)
        if curr_sum % K == 0:
            res += r - l + 1
        while curr_sum % K == 0 and l <= r:
            curr_sum -= A[l]
            # print("After subtracting", curr_sum)
            l += 1
        r += 1
    return res


if __name__ == '__main__': 
    print(subarraysDivByK_optimal([4, 5, 0, -2, -3, 1], 5))
    print(subarraysDivByK_optimal([5], 9))