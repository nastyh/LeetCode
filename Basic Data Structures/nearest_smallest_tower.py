def find_nearest_shorter_tower(heights):
    """
    O(n) both 
    Left Nearest Shorter Tower:
    Traverse the array from left to right, maintaining a stack of indices.
    Pop from the stack while the current height is less than or equal to the height at the index on top of the stack.
    The top of the stack gives the nearest shorter tower to the left.
    
    Right Nearest Shorter Tower:
    Traverse the array from right to left similarly, maintaining a stack of indices.
    The top of the stack gives the nearest shorter tower to the right.
    Choosing the Result:

    For each tower, compare the indices of the nearest shorter towers to the left and right.
    Use the rules provided to determine the final index for each tower.
    """
    n = len(heights)
    result = [-1] * n
    
    # Helper function to find nearest shorter tower indices
    def find_nearest_side(heights, direction):
        stack = []
        nearest = [-1] * n
        
        # Iterate in the appropriate direction
        indices = range(n) if direction == "left" else range(n - 1, -1, -1)
        
        for i in indices:
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nearest[i] = stack[-1]
            stack.append(i)
        
        return nearest
    
    # Find nearest shorter tower to the left
    left_nearest = find_nearest_side(heights, "left")
    
    # Find nearest shorter tower to the right
    right_nearest = find_nearest_side(heights, "right")
    
    # Determine the final result based on the rules
    for i in range(n):
        left = left_nearest[i]
        right = right_nearest[i]
        
        if left == -1 and right == -1:
            result[i] = -1
        elif left == -1:
            result[i] = right
        elif right == -1:
            result[i] = left
        else:
            left_distance = abs(i - left)
            right_distance = abs(i - right)
            
            if left_distance < right_distance:
                result[i] = left
            elif right_distance < left_distance:
                result[i] = right
            else:
                # If distances are the same, choose the tower with smaller height
                if heights[left] < heights[right]:
                    result[i] = left
                elif heights[right] < heights[left]:
                    result[i] = right
                else:
                    # If heights are the same, choose the smaller index
                    result[i] = min(left, right)
    
    return result
