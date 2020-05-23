from heapq import heappop, heappush, nlargest, nsmallest
def topKFrequent(words, k):
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    # res = [k for k, v in sorted(d.items(), reverse = True, key = lambda x: x[1])][:k]
    # return sorted(res)


    #alternative
    return nsmallest(k, d.keys(), key = lambda x: (-d[x], x))

    # with heaps too
    heap = []
    heapq.heapify(heap)
    for key in d:
        heapq.heappush(heap, (-d[key], key))
        # pop top k
        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped)
        # sort res alphabetically
        res.sort()
        newres = []
        for word in res:
            newres.append(word[1])
        return newres



if __name__ == '__main__':
    # print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    # print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
