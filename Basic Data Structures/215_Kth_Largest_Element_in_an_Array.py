from heapq import heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heap_sort(arr):
            heap = []
            for el in arr:
                heappush(heap, el)

            ordered = []
            while heap:
                ordered.append(heappop(heap))
            return ordered
        return heap_sort(nums)[-k]
