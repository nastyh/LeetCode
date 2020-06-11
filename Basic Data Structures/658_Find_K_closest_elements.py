def findClosestElements(arr, k, x):
    distances = []
    for num in arr:
        distance = abs(x - num)
        distances.append(distance)
    zipped = zip(distances, arr)
    sorted_zipped = [x for _, x in sorted(zipped)]
    return sorted(sorted_zipped[:k])

def findClosestElements_bin_search(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = left + (right - left) // 2

        # mid + k is closer to x, discard mid by assigning left = mid + 1
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1

        # mid is equal or closer to x than mid + k, remains mid as candidate
        else:
            right = mid

    # left == right, which makes both left and left + k have same diff with x
    return arr[left : left + k]


if __name__ == '__main__':
    print(findClosestElements([1,2,3,4,5], 4, 3))
    print(findClosestElements_bin_search([1,2,3,4,5], 4, 3))
