def get_minimum_manhattan_distance(positions):
    """
    O(nlogn) to  sort
    O(n) to store the coordinates
    
    """
    # Extract x and y coordinates
    x_coords = [x for x, y in positions]
    y_coords = [y for x, y in positions]
    
    # Find the medians of x and y
    x_coords.sort()
    y_coords.sort()
    median_x = x_coords[len(x_coords) // 2]
    median_y = y_coords[len(y_coords) // 2]
    
    # Calculate the total Manhattan distance to the median point
    total_distance = sum(abs(x - median_x) + abs(y - median_y) for x, y in positions)
    
    return total_distance

# Example usage
positions = [[0, 1], [1, 0], [1, 2], [2, 1], [1, 1]]
print(get_minimum_manhattan_distance(positions))  # Output: 6
