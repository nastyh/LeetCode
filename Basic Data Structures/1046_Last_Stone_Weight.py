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


def lastStoneWeight_another_heap(self, stones: List[int]) -> int:
    """
    O(nlogn) both since it's a heap
    it's a max heap, thus, with the negative values
    We take out the elements in pairs, so need to make sure the heap
    always has at least two elements. So we have the while loop
    At the end, the heap will either have two or one elements left.
    Process both variants manually 
    """
    if len(stones) == 1: return 1
    h = []
    for stone in stones:
        heapq.heappush(h, -stone)
    while len(h) > 2:
        y_stone = - heapq.heappop(h)
        x_stone = - heapq.heappop(h)
        if x_stone < y_stone:
            heapq.heappush(h, -(y_stone - x_stone))
    if len(h) == 2:
        return -heapq.heappop(h) - (-heapq.heappop(h))
    else:
        return -heapq.heappop(h)
        
def lastStoneWeight_sorting(stones):  # O(nlogn) and O(1)
    while len(stones) !=1:
        stones = sorted(stones)
        last= stones.pop()
        stones[len(stones)-1] = last - stones[len(stones)-1]
    return stones[0]
