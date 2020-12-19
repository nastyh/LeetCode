def search_min_diff_element(arr, key):
    """
    Cover two edge cases
    Do a normal binary search
    At the end, if the exact number hasn't been found, compare left and right indices 
    """
    if key < arr[0]:
        return arr[0]
    if key > arr[-1]:
        return arr[-1]
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] - key == 0:
            return arr[m]
        elif arr[m] - key < 0:
            l = m + 1
        else:
            r = m - 1
    if (arr[l] - key) < (key - arr[r]):
        return arr[l]
    return arr[r]


if __name__ == '__main__':
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))