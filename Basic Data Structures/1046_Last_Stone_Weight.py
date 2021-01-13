def lastStoneWeight(stones):  # O(NlogN) to create a heap and take out elements up to N - 1 times. Space is O(logn) for heaps in Python
    """
    make a heap
    take out two largest elements (accurate with minus signs)
    if there is a leftover, add it back to the heap
    If there is one element left, it's the largest element, return it. Otherwise, 0
    """
    h = []
    for stone in stones:
        heapq.heappush(h, -stone)
    while len(h) > 1:
        x = -heapq.heappop(h)
        y = -heapq.heappop(h)
        if x - y > 0:
            heapq.heappush(h, -(x - y))
    return -heapq.heappop(h) if h else 0


def lastStoneWeight_sorting(stones):  # O(nlogn) and O(1)
    while len(stones) !=1:
        stones = sorted(stones)
        last= stones.pop()
        stones[len(stones)-1] = last - stones[len(stones)-1]
    return stones[0]
