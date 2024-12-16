class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        O(nlogn) for the heap
        O(n) for res (not necessarily, can update nums on the go)
        res is the copy of nums first
        key is throw both the values and the indices into the heap
        Take out the smallest element and its index in nums
        Put into the same place inside res the value that is whatever is there times multiplier
        put back into the heap this new value and the respective index
        """
        res = [num for num in nums]
        h = [(val, ix) for ix, val in enumerate(nums)]
        heapq.heapify(h)
        for _ in range(k):
            curr_smallest_val, ix_of_curr_smallest_value = heapq.heappop(h)
            res[ix_of_curr_smallest_value] *= multiplier 
            heapq.heappush(h, (res[ix_of_curr_smallest_value], ix_of_curr_smallest_value))
        return res

     def getFinalState_no_res(self, nums: List[int], k: int, multiplier: int) -> List[int]:
         """
         same but we can update the nums on the go
         """
        h = [(val, ix) for ix, val in enumerate(nums)]
        heapq.heapify(h)
        for _ in range(k):
            _, ix_of_curr_smallest_value = heapq.heappop(h)
            nums[ix_of_curr_smallest_value] *= multiplier 
            heapq.heappush(h, (nums[ix_of_curr_smallest_value], ix_of_curr_smallest_value))
        return nums 