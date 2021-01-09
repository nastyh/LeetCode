import heapq
def findClosestElements(arr, k, x):  # O(nlogn) and O(k), k-length sublist
    distances = []
    for num in arr:
        distance = abs(x - num)
        distances.append(distance)
    zipped = zip(distances, arr)
    sorted_zipped = [x for _, x in sorted(zipped)]
    return sorted(sorted_zipped[:k])

def findClosestElements_bin_search(arr, k, x):  # O(logn + k). Bin search + shrinking the index range to k elements. Space O(k)
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


def findClosestElements_heap(arr, k, x):  # Still O(nlogn) due to sorted at the end. O(k)
    h, res = [], []
    for num in arr:
        heapq.heappush(h, (abs(x - num), num))
    for _ in range(k):
        diff, num = heapq.heappop(h)
        res.append(num)
    ans = sorted(res)
    return ans


if __name__ == '__main__':
    print(findClosestElements([1, 2, 3, 4, 5], 4, 3))
    print(findClosestElements_bin_search([1, 2, 3, 4, 5], 4, 3))
    print(findClosestElements_heap([1, 2, 3, 4, 5], 4, 3))
