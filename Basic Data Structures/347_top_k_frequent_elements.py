class Solution:
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]: # O(nlogk) both
        # have a dict of item: number of times
        d, h, res = Counter(nums), [], []
        for key, v in d.items():
            # maintain a heap of the length k
            # is contains a tuple (v, key)
            # means it will always contain k max elements by frequency 
            # it works since we can return results in any order
            if len(h) < k:
                heapq.heappush(h, (v, key))
            else:
                heapq.heappushpop(h, (v, key))
        # build your answer 
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res

    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]: 
        d, res = Counter(nums), []
        # list of the keys that are sorted by their respective frequencies
        d_sorted = [k for k, v in sorted(d.items(), key = lambda x: x[1], reverse = True)]
        # return only the first k of them
        return d_sorted[:k]

    def topKFrequent_another_heap(self, nums: List[int], k: int) -> List[int]: 
        """
        since by default it's a min heap, we need to keep it with an opposite sign
        this solution respects the order. We return the results from the largest
        frequency to the lowest one
        """
        d = Counter(nums)
        hp = []
        for key, v in d.items():
            heapq.heappush(hp, (-v, key))
        # Popping out all the number for  value k
        res = []
        for _ in range(k):
            x, y = heapq.heappop(hp)
            res.append(y)
        return res