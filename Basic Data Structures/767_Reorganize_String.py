def reorganizeString(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s

    i, res, n = 0, [None] * len(s), len(s)

    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    for k in sorted(d, key = d.get, reverse = True):
        if d[k] > n // 2 + n % 2: # if the element's count is more than half of the length of the list plus 1
            return ''
        for j in range(d[k]):
            if i >= n:
                i = 1
            res[i] = k
            i += 2
    return ''.join(res)


# with heap
import heapq
def reorganizeStringHeap(S):
    dictionary = {}
    heap = []

    for value in S:
        dictionary[value] = dictionary.get(value, 0) + 1

    for k,v in dictionary.items():
        heap.append([-v,k]) # most frequent is on top

    heapq.heapify(heap)

    res = ''
    while(heap):
        if len(heap)>=2:
            value_1 = heapq.heappop(heap)
            res += value_1[1]
            value_2 = heapq.heappop(heap)
            res += value_2[1]

            value_1[0] += 1
            value_2[0] += 1

            if value_1[0] != 0:
                heapq.heappush(heap, [value_1[0], value_1[1]])
            if value_2[0] != 0:
                heapq.heappush(heap, [value_2[0], value_2[1]])

        elif len(heap) == 1:
            value_1 = heapq.heappop(heap)
            res+=value_1[1]
            value_1[0] += 1
            if value_1[0] != 0:
                return ""

            return res
    return res



    # return sorted(d, key = d.get, reverse = True)

if __name__ == '__main__':
    print(reorganizeString('aaaccccbb'))
    print(reorganizeStringHeap('aaaccccbb'))
