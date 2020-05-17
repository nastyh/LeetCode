def sortedArrays(lists, m): # brute force
    res = []
    for l in lists:
        res.extend(l)
    sorted_res = sorted(res)
    return sorted_res[m-1]

import heapq
def sortedArrays_heap(lists, m): # using heaps
    res = []
    for l in lists:
        res.extend(l)
    h = []
    for value in res:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(m)][-1]


if __name__ == '__main__':
    print(sortedArrays([[3,4,5], [23, 24, 29]], 5))
    print(sortedArrays_heap([[3,4,5], [23, 24, 29]], 5))
