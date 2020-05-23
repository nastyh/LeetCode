import heapq
def topKFrequent(nums, k):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    d_sorted = [k for k, v in sorted(d.items(), key = lambda x: x[1], reverse = True)]
    return d_sorted[:k]


#alt
    if not nums: return []

    freq = dict(collections.Counter(nums))

    pq = []
    for i in freq.keys():
        heapq.heappush(pq, (freq[i], i))
        if len(pq) > k:
            heapq.heappop(pq)

    result = list()
    for i in range(k-1, -1, -1):
        result.append(pq[i][1])

    return result

if __name__ == '__main__':
    print(topKFrequent([1,1,1,2,2,3], 2))
