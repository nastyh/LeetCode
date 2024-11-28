def reorganizeString_detailed(self, s: str) -> str:
    """
    O(nlog(lens(k))) k is only 26, so we can say complexity is O(n), where n is the length of s
    O(k) for dict, but it's only 26 chars, so can say O(1)
    build frequency dict: {a: 2, b: 1} for "aab"
    throw into a heap, with an opposite sign so we have fast access to the most frequent element 
    """
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s
    res = []
    d = Counter(s)
    h = []
    for k, v in d.items():
        h.append([-v, k]) 
    heapq.heapify(h) # [[-2, a], [-1, b]]
    while h:
        if len(h) >= 2: # while we have anything to combine
            el1 = heapq.heappop(h) # most frequent element
            res.append(el1[1]) # build the answer
            el2 = heapq.heappop(h) # next most frequent element
            res.append(el2[1]) # build the answer
            # update the counts of the chars used
            el1[0] += 1
            el2[0] += 1
            # push the updated results back to the heap
            if el1[0] != 0:
                heapq.heappush(h, [el1[0], el1[1]])
            if el2[0] != 0:
                heapq.heappush(h, [el2[0], el2[1]]) 
        elif len(h) == 1: # we ran out of certain letters
            el1 = heapq.heappop(h)
            res.append(el1[1])
            el1[0]+=1
            if el1[0] != 0: # left with an unmatched char
                return "" # cannot do it
            else: return ''.join(ch for ch in res)
    return ''.join(ch for ch in res)

def reorganizeString(s):  # O(nlogn) b/c of sorting and O(n) 
    """
    Need to process greedily: most frequently occured char is mixed with the second most frequently occured character, etc. 
    """
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
def reorganizeStringHeap(S):  # O(NLog A) and O(A) where A is the size of the alphabet. If A is fixed, than time is O(N)
    dictionary = {}
    heap = []
    for value in S:
        dictionary[value] = dictionary.get(value, 0) + 1
    for k,v in dictionary.items():
        heap.append([-v,k]) # most frequent is on top
    heapq.heapify(heap)
    res = ''
    while(heap):
        if len(heap) >= 2:
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
