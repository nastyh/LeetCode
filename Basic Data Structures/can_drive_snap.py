"""
https://leetcode.com/discuss/post/5363875/snap-phone-screen-road-blocks-on-an-infi-03jy/
There's a very long road along y-axis, bounded between x-axis from [0, 100]
A driver tries to drive from the start of this road to the end.
Given a list of rectangle blockers, will the driver be able to make it to the end?
Rectangles are parallel to x and y axis. They are represented by 4 floats (bottom_left_x, bottom_left_y, top_right_x, top_right_y)
Hint by the interviewer: We can say that the road is blocked completely by the rectangular blocks, if we can walk from x = 0 to x = 100.
"""

def can_drive_to_end(rectangles):
    """
    O(nlogn) due to sort
    Space is o(n) to store rectangles and merged intervals
    """
    # Represent the start and end points of the road
    road_start = 0
    road_end = 100

    # Sort rectangles by bottom-left x-coordinate
    intervals = []
    for rect in rectangles:
        bottom_left_x, bottom_left_y, top_right_x, top_right_y = rect
        if bottom_left_x < road_end and top_right_x > road_start:
            # We care about rectangles that intersect the road (x = 0 to x = 100)
            intervals.append((max(bottom_left_x, road_start), min(top_right_x, road_end), bottom_left_y, top_right_y))
    
    # Sort intervals by x-coordinates
    intervals.sort()

    # Sweep line algorithm to merge intervals
    current_x = road_start
    current_y_intervals = []
    
    for interval in intervals:
        x_start, x_end, y_start, y_end = interval
        # If current_x can get from x_start to x_end without being blocked, then pass
        if current_x < x_start:
            # There's a gap in the intervals
            current_x = x_end
            continue
        
        # Merge the y-ranges of the overlapping intervals
        if current_y_intervals and current_y_intervals[-1][1] >= y_start:
            current_y_intervals[-1] = (current_y_intervals[-1][0], max(current_y_intervals[-1][1], y_end))
        else:
            current_y_intervals.append((y_start, y_end))
        
        # Move the road end point to right after this interval
        current_x = x_end

    # After the merge, check if there is a valid gap to move
    return current_x >= road_end
