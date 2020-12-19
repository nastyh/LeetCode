"""
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
"""
def find_max_in_bitonic_array(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = l + (r - l) // 2
        if arr[m] > arr[m + 1]:
            r = m
        else:
            l = m + 1
    return arr[l]


if __name__ == '__main__':
    print(find_max_in_bitonic_array([1, 3, 8 ,12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8 ,12]))
    print(find_max_in_bitonic_array([10, 9, 8]))