from collections import defaultdict
import heapq


class NumberContainers:
    """
    Change and Find both are
    O(logN), N num of indices assocated with a given num. Due to the heap
    O(M) num of the total change calls
    """

    def __init__(self):
        self.d_nums = defaultdict(list) # number: [heap of indices] --> to access the smallest ix
        self.d_ix = {} # ix: number, other way around, given index and currently associated with it numbertete

    def change(self, index: int, number: int) -> None:
        """
        If ix is already associated with an old num, remove it from the heap 
        Upadate d_ix to include a new association
        Push the index into the heap of indices associated with this number
        """
        if index in self.d_ix:
            old_num = self.d_ix[index]
            if old_num != number:
                self._remove_ix(old_num, index)
        self.d_ix[index] = number
        heapq.heappush(self.d_nums[number], index)
    
    def _remove_ix(self, number: int, index: int) -> None:
        """
        Helper 
        we cannot efficiently remove an element from a min heap directly
        push a dummy var inf to force the cleanup 
        """
        heap = self.d_nums[number]
        heapq.heappush(heap, float('inf'))  
        while heap and heap[0] == float('inf'): # removing indices associated with a number till only inf left in the heap
            heapq.heappop(heap)
        
    def find(self, number: int) -> int:
        """
        Clean up the min heap by popping invalid or stale indices
        If the index at the top of the heap (heap[0]) is marked for lazy deletion
        (float('inf')) or if it no longer maps to the current number, remove it.
        """
        heap = self.d_nums[number]
        # Clean up invalid entries before returning the smallest valid index
        while heap and (heap[0] == float('inf') or self.d_ix[heap[0]] != number):
            heapq.heappop(heap)  # Remove stale or invalid indices
        # Return the smallest valid index, or -1 if no valid index exists
        if heap:
            return heap[0]
        return -1