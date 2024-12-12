class Solution:
    def pickGifts_heap(self, gifts: List[int], k: int) -> int:
        """
        O(n + klogn) O(n) to initialize the heap. Push and pop are O(logn) both since it's a balanced binary tree
        Perform it k times 
        O(n) for the heap containing n elements 
        Throw everything in a heap with an opposite sign so we have access to the largest element 
        take it out, put back the square root of this number and do it k times 
        What is left in the heap is the answer (but it's with an opposite sign)
        """
        h = [- g for g in gifts]
        heapq.heapify(h)
        for _ in range(k):
            curr_max = - heapq.heappop(h)
            heapq.heappush(h, -math.floor(math.sqrt(curr_max)))
        res = 0
        while h:
            res += heapq.heappop(h)
        return -res

    def pickGifts_deque(self, gifts: List[int], k: int) -> int:
        d = deque()
        taken = 0
        for g in gifts:
            d.append(-g)
        for _ in range(k):
            t = d.popleft()
            taken += math.floor(math.sqrt(-t))
            d.append(-math.floor(math.sqrt(-t)))
        res = 0
        while d:
            res += d.popleft()
        return -d

    def pickGifts_sorting(self, gifts: List[int], k: int) -> int:
        """
        O(n + klogn)
        O(n)
        """
        sorted_gifts = sorted(gifts)
        largest_gift = gifts[-1]
        for _ in range(k):
            max_element = sorted_gifts[-1]
            sorted_gifts.pop()
        ix_of_sqrt =  next(
                (
                    i
                    for i, value in enumerate(sorted_gifts)
                    if value > math.floor(math.sqrt(max_element))
                ),
                n,
            )
        sorted_gifts.insert(
                ix_of_sqrt, math.floor(math.sqrt(max_element))
            )
        # Calculate the sum of the remaining elements in the sorted array
        number_of_remaining_gifts = sum(sorted_gifts)
        return number_of_remaining_gifts
