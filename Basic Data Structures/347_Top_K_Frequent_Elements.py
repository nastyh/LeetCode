import heapq
def topKFrequent(nums, k):  # O(Nlog(N)) where n is the length of nums
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    d_sorted = [k for k, v in sorted(d.items(), key = lambda x: x[1], reverse = True)]
    return d_sorted[:k]


#alt
    # if not nums: return []

    # freq = dict(collections.Counter(nums))

    # pq = []
    # for i in freq.keys():
    #     heapq.heappush(pq, (freq[i], i))
    #     if len(pq) > k:
    #         heapq.heappop(pq)

    # result = list()
    # for i in range(k-1, -1, -1):
    #     result.append(pq[i][1])

    # return result

# easier to understand

def topKFrequent_heap(nums, k): 
    """
    Build a dictionary, start adding elements with frequencies to a heap.
    Because the heap is the min heap by default, add frequencies with an opposite sign
    Then start popping out elements till you have k elements and return them
    O(n) space
    To add k elements to the heap takes O(k) on average, and KlogK in the worst case
    Heap push/pop is O(logK) and we do it N - K times --> O((N - K)logK)
    Overall end up with O(KlogK) in time complexity
    """
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    hp = []
    for key,v in d.items():
        heapq.heappush(hp,(-v,key))
    # Popping out all the number for  value k
    res = []
    for _ in range(k):
        x, y = heapq.heappop(hp)
        res.append(y)
    return res


if __name__ == '__main__':
    # print(topKFrequent([1,1,1,2,2,3], 2))
    # print(topKFrequent_heap([-1,-1], 1)) # [1,1,1,2,2,3], 2
    print(topKFrequent_heap([1, 1, 1, 2, 2, 3], 2))
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
