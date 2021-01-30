import heapq
from collections import Counter
def topKFrequent(nums, k):  # O(Nlog(N)) where n is the length of nums
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    d_sorted = [k for k, v in sorted(d.items(), key = lambda x: x[1], reverse = True)]
    return d_sorted[:k]


def topKFrequent_optimal(nums, k): # O(nlogk) and O(n)
    if k == len(nums):
        return nums
    d = Counter(nums)   
    return heapq.nlargest(k, d.keys(), key = d.get) 


    # h, res = [], []
    # d = Counter(nums)
    # print(d)
    # for ix, v in d.items():
    #     if len(h) < k:
    #         heapq.heappush(h, (-v, ix))
    #         print(h)
    #     else:
    #         if -v < h[0][0]:
    #             # print(-v)
    #             heapq.heappop(h)
    #             heapq.heappush(h, (-v, ix))
    #         elif -v == h[0][0]:
    #             heapq.heappush(h, (-v, ix))
    #         else:
    #             continue
    #         # heapq.heappushpop(h, (-v, ix))
    # print(h)
    # for _ in range(k):
    #     res.append(heapq.heappop(h)[1])
    # return res

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
    # print(topKFrequent_heap([1, 1, 1, 2, 2, 3], 2))
    # print(topKFrequent_optimal([1, 1, 1, 2, 2, 3], 2))
    # print(topKFrequent_optimal([3, 0, 1, 0], 1))
    # print(topKFrequent_optimal([4, 1, -1, 2, -1, 2, 3], 2))
    print(topKFrequent_optimal([5, 3, 1, 1, 1, 3, 73, 1], 2))
    # print(topKFrequent_optimal([1], 1))
    # print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
