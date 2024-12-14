class Solution:
    def continuousSubarrays_heap(self, nums: List[int]) -> int:
        """
        O(nlogn) and O(n)
        poorly worded question
        what it actually means is that the abs diff between the largest
        and the smallest element in a subarray should be <= 2
        two heaps to have access to the min and the max elements and their indices
        two pointers to create a sliding window 
        throw in nums[r] and r into both heaps
        while l < r and diff between max and min values <=2:
            move the left pointer
            remove outdated pairs from both heaps 
        everything valid ends at index r, overall it's r - l + 1
        move r
        """
        l, r, res, h_min, h_max = 0, 0, 0, [], []
        while r < len(nums):
            heapq.heappush(h_min, (nums[r], r))
            heapq.heappush(h_max, (-nums[r], r))

            while l < r and -h_max[0][0] - h_min[0][0] > 2:
                l += 1
                while h_min and h_min[0][1] < l:
                    heapq.heappop(h_min)
                while h_max and h_max[0][1] < l:
                    heapq.heappop(h_max)
            res += r - l + 1
            r += 1
        return res
    def continuousSubarrays_2pointers(self, nums: List[int]) -> int:
        """
        O(n)
        O(1)
         Each time we add a new element, we have two possibilities: either it maintains the condition that the 
         max−min≤2, or it breaks this condition. When the condition breaks, we know that all previous subarrays
         up to that point form a complete, valid window. This gives us our first key insight:
         we can count all the subarrays before that point and add them to our result. To count all
         subarrays in a window of length n, we can use the formula n⋅(n+1)/2.
         when the condition breaks, instead of starting completely fresh, we can expand
         backward from our current position to include some previous elements. 
         after a window breaks, we can greedily expand leftward as long as elements remain within 2 of our current value. 
         When we expand backward, we've already counted some subarrays in our previous window that we'll
         count again in our new window. The solution is simple: we subtract the overcounted subarrays using
         the same n⋅(n+1)/2 formula for the overlapping portion.


        """
        res = 0
        l = 0
        window_length = 0
        curr_min = curr_max = nums[0]
        for r in range(len(nums)):
            curr_min = min(curr_min, nums[r])
            curr_max = max(curr_max, nums[r])

            if curr_max - curr_min > 2: # condition breaks 
                window_length = r - l # subarrays from the previous valid window
                res += window_length * (window_length + 1) // 2

                l = r
                curr_min = curr_max = nums[r]

                while l > 0 and abs(nums[r] - nums[l - 1]) <= 2:
                    l -= 1
                    curr_min = min(curr_min, nums[l])
                    curr_max = max(curr_max, nums[l])

                if l < r: # remove overcounts subarrays if the left pointer expanded 
                    window_length = r - l
                    res -= window_length * (window_length + 1) // 2
        window_length = r - l + 1
        res += window_length * (window_length + 1) // 2
        return res 
