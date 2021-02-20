import heapq

def frequencySort_pythonic(s):
    d = Counter(s)
    res = []
    for key, value in sorted(d.items(), key = lambda x : x[1], reverse = True):
        res.append(key * value)
    return ''.join(res)
    

def frequencySort(s):
    d  = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1

    # return ''.join([k for k,v in sorted(d.items(), key = lambda x: x[1], reverse = True)])
    return ''.join([k * v for k,v in sorted(d.items(), key = lambda x: x[1], reverse = True)])

    # using heap
def frequencySort_heap(s):
    d  = {}
    for ch in s:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    hp, res = [], ''
    for k, v in d.items():
        heapq.heappush(hp, (-v, k))
    while hp:
        v, k = heapq.heappop(hp)
        res += ''.join(k * -v)
    return res


def frequencySort_heap_fastest(s):  # O(nlogn) b/c we add all elements to the heap. O(n) space 
    """
    It's faster to maintain a normal heap and reverse the string at the end so that more frequent lettes go first
    """
    d = Counter(s)
    h, res = [], ''
    for k, v in d.items():
        heapq.heappush(h, (v, k))
    while h:
        ch, freq = heapq.heappop(h)
        res += ch * freq
    return res[::-1]


if __name__ == '__main__':
    print(frequencySort('tree'))
    print(frequencySort_heap('tree'))
