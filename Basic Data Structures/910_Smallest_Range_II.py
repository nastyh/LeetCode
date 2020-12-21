def smallestRangeII(A, K):  # O(nlogn)
    A.sort()
    l, r = A[0], A[-1]
    ans = r - l
    for i in range(len(A) - 1):
        a, b = A[i], A[i + 1]
        ans = min(ans, max(r - K, a + K) - min(l + K, b - K))
    return ans



if __name__ == '__main__':
    print(smallestRangeII([1], 0))
    print(smallestRangeII([0, 10], 2))
    print(smallestRangeII([1, 3, 6], 3))