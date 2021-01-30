from collections import Counter
from heapq import heappop, heappush, nlargest, nsmallest
def topKFrequent(words, k):  # O(N + klogN) b/c heapify and counting are O(N) and each heappop() in logk. and O(N)
    d = Counter(words)
    # res = [k for k, v in sorted(d.items(), reverse = True, key = lambda x: x[1])][:k]
    # return sorted(res)
    #alternative
    return nsmallest(k, d.keys(), key = lambda x: (-d[x], x))


def topKFrequent_alt(words, k):  # O(N + klogN) b/c heapify and counting are O(N) and each heappop() in logk. and O(N)
    d = Counter(words)
    h = []
    for word, ix in d.items():
        heapq.heappush(h, (-ix, word))
    return [heapq.heappop(h)[1] for _ in range(k)]



if __name__ == '__main__':
    # print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    # print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
