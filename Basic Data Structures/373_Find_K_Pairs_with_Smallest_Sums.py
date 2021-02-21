import heapq
def kSmallestPairs(nums1, nums2, k):
    min_heap = []
    # If either of the arrays are empty then return empty list
    if not nums1 or not nums2:
        return []
    # Add the first row of the sum matrix to the heap [fix i = 0 and move j, which is adds 3,5,7]
    for j in range(len(nums2)):
        heapq.heappush(min_heap, [nums1[0] + nums2[j], 0, j])
    pairs = []
    while min_heap and k > 0:
        # pop from heap, NB the heap uses the first value (nums1[0] + nums2[j]) to validate heap property.
        min_sum, i, j = heapq.heappop(min_heap)
        # Now append the pairs that just popped out of the heap
        pairs.append([nums1[i], nums2[j]])
        # Now move to the next row (9,11,13) by increamenting the i by 1
        if i + 1 < len(nums1):
            heapq.heappush(min_heap, [nums1[i + 1] + nums2[j], i + 1, j] )
        k -= 1
    return pairs


def kSmallestPairs_alt(nums1, nums2, k):  # O((logn * logm)) and O(mn) most likely 
    """
    Brute force: put everything in a heap, then take out
    Edge case is to write range(min(k, len(h))) to handle a case when we have fewer elements than k 
    """
    h, res = [], []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            heapq.heappush(h, (nums1[i] + nums2[j], [nums1[i], nums2[j]]))
    for _ in range(min(k, len(h))):
        _, pair = heapq.heappop(h)
        res.append(pair)
    return res


def kSmallestPairs_pythonic(nums1, nums2, k):
    list1 = [] 
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            list1.append([nums1[i], nums2[j]])        
    return heapq.nsmallest(k, list1, key = lambda x : sum(x))


if __name__ == '__main__':
    # print(kSmallestPairs([1, 2], [3], 3))
    # print(kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
    # print(kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
    print(kSmallestPairs_alt([1, 7, 11], [2, 4, 6], 3))
    print(kSmallestPairs_alt([1, 1, 2], [1, 2, 3], 2))
    print(kSmallestPairs_alt([1, 2], [3], 3))
