def findKthPositive(arr, k):  # O(n) and O(1)
    """
    Brute force:
    keep iterating through the elements and decrease k.
    If k == 0, then it's time to return the result
    Edge case is when the result is outside the max(arr)
    Then just keep incrementing max(arr) the required number of times 
    """
    res = None
    for num in range(1, max(arr) + 1):
        if num not in arr:
            k -= 1
            res = num
        if k == 0:
            if res is not None:
                return res
    res = max(arr)
    for _ in range(max(arr), max(arr) + k):
        res += 1
    return res


def findKthPositive_bin_search(arr, k):  # O(logn) and O(1)
    """
    ideally, arr[i] should hold i + 1 value i.e arr[0] = 1, arr[1] = 2..etc
    arr = [2, 3, 4, 7, 11], k = 5
    missing = arr[mid] - (mid + 1)
    We get mid=2 at the first loop, and missing value 1 means that until index 2(mid), we can get 1 missing number.
    which means... ideally arr[2] holds 3, but it holds 4. So, the number of missing value is 1.
    """
    lo = 0
    hi = len(arr) - 1
    while(lo <= hi):
        mid = lo + (hi - lo) // 2
        missing = arr[mid] - (mid + 1)  # ideally, arr[i] should hold i + 1 value i.e arr[0] = 1, arr[1] = 2..etc
        if missing >= k:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi + k + 1

if __name__ == '__main__':
    print(findKthPositive([2, 3, 4, 7, 11], 5))
    print(findKthPositive([1, 2, 3, 4], 2))
    print(findKthPositive_bin_search([2, 3, 4, 7, 11], 5))
    print(findKthPositive_bin_search([1, 2, 3, 4], 2))