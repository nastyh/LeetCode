class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        O(nlogn)
        O(N)
        ladder for the longest climbs
        bricks for the shortest climbs 
        we should ensure ladders have been allocated to the longest climbs
        seen so far and bricks to the shortest.
        To find all climbs, we'll need to check the difference between
        each adjacent (side-by-side) pair of buildings to see if there is 
        a climb there or a jump down/ walk across.
        min heap
        compare buildings next to each other 
        if diff < 0, nothing needs to be done, we go down 
        otherwise, use the ladders if possible
        finally, use the bricks first for the smallest positive height_diff
        we've encountered so far 
        """
        h = []
        for i in range(len(heights) - 1):
            curr_height = heights[i]
            next_height = heights[i + 1]
            height_diff = next_height - curr_height
            if height_diff <= 0: 
                continue
            heapq.heappush(h, height_diff)
            to_climb = height_diff 
            if len(h) <= ladders:
                continue 
            bricks = bricks - heapq.heappop(h)
            if bricks < 0:
                return i
        return len(heights) - 1