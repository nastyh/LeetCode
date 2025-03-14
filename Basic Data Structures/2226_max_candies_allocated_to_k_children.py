from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        O(nlogM), n num of elements in candies, M the max number of candies in any pile
        O(1) no extra space
        binary search:
        low: 0 per child to maximize the count
        high: max of candies -- it's what any child could receive 
        The loop continues as long as low is less than or equal to high
        Mid Calculation: The candidate number of candies per child is calculated as the average of low and high.
        For each pile in candies, the number of children that can receive mid candies is determined by integer division (c // mid).
        The sum of these values gives the total number of children that can be served with mid candies each.
        if count >=k:
        it is possible to give at least k children mid candies each.
        Update result to mid because it's a valid candidate.
        Increase low to mid + 1 to try and see if a higher candidate value is possible.
        if count < k
        candidate mid is too high to serve k children.
        Decrease high to mid - 1 to try lower candidate values.
        return res
        """
        if not candies:  # edge case
            return 0
    
        low, high = 1, max(candies)
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            count = sum(c // mid for c in candies)
            
            # If it's possible to give at least k children mid candies each.
            if count >= k:
                result = mid   # Update result because mid is a valid candidate.
                low = mid + 1  # Try for a higher value.
            else:
                high = mid - 1  # Lower the candidate.
        
        return result