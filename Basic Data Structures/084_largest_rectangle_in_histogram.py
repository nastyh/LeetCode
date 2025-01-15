from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        O(n) both 
        Traverse the histogram from left to right.
        Use a stack to keep track of indices of the bars.
        For each bar:
        If the current bar is taller than the bar at the index stored at the top of the stack, push its index onto the stack.
        If the current bar is shorter, calculate the area for the rectangle with the height of the bar at the top of the stack
        as the smallest height. Pop the top index and calculate the width based on the current index and the index now at
        the top of the stack.
        After the loop, process any remaining bars in the stack to calculate their rectangle areas.
        """
        stack = []  # Stack to store indices of histogram bars
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                # Pop the top of the stack
                top = stack.pop()
                # Calculate the height of the rectangle
                height = heights[top]
                # Calculate the width of the rectangle
                width = i if not stack else i - stack[-1] - 1
                # Update max_area
                max_area = max(max_area, height * width)
            stack.append(i)
        
        # Process remaining elements in the stack
        while stack:
            top = stack.pop()
            height = heights[top]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area