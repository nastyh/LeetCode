import heapq
def kSmallestPairs(nums1, nums2, k):
    nums1.sort()
    nums2.sort()
    h = []
    for i in range(min(len(nums1), len(nums2))):
        h.append((nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        heapq.heapify(h)
    output = []
    while k > 0 and len(h) > 0:
        _, n1, n2, idx = heapq.heappop(h)
    output.append([n1, n2])
    if idx + 1 < len(nums2):
        n2 = nums2[idx+1]
        heapq.heappush(h, (n1 + n2, n1, n2, idx + 1))
        k -= 1
    return output


if __name__ == '__main__':
    print(kSmallestPairs([1, 2], [3], 3))
    print(kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
    print(kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
