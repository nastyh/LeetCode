class Solution:
    def findScore_sorting(self, nums: List[int]) -> int:
        """
        O(nlogn)
        O(n) for marked
        Just simulate the process
        Key is to have sorted_nums with tuples of num, ix since we needd to handle 
        when there are two equal numbers and we need the smallest one
        Then sort this thing
        Go one by one, add to res, mark as marked, then
        if you can go left, mark the left one
        if you can go right, mark the right one, too
        """
        res = 0
        sorted_nums = [(num, idx) for idx, num in enumerate(nums)]
        sorted_nums.sort()
        marked = [0] * len(nums)
        for i in range(len(nums)):
             curr_num = sorted_nums[i][0]
             curr_ix = sorted_nums[i][1]
             if marked[curr_ix] == 0:
                res += curr_num
                marked[curr_ix] = 1
                if curr_ix - 1 >= 0:
                    marked[curr_ix - 1] = 1
                if curr_ix + 1 < len(nums):
                    marked[curr_ix + 1] = 1
        return res

    def findScore_heap(self, nums: List[int]) -> int:
        """
        O(nlogn)
        O(n) for marked
        Same thing but instead of .sort()
        use a heap
        it does by value first, then, if there is a tie, by the index
        """
        h, res, marked = [], 0, [0] * len(nums)
        for ix, num in enumerate(nums):
            h.append((num, ix))
        heapq.heapify(h) # smallest values comes first
        while h:
            curr_num, curr_ix = heapq.heappop(h)
            if marked[curr_ix] == 0:
                res += curr_num
                marked[curr_ix] = 1
                if curr_ix - 1 >= 0:
                    marked[curr_ix - 1] = 1
                if curr_ix + 1 < len(nums):
                    marked[curr_ix + 1] = 1
        return res

