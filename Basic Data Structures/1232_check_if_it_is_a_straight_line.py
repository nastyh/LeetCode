class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True  # Two points always define a line
        # Extract the first two points
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        # Handle vertical lines
        if x1 - x0 == 0:
            for x, y in coordinates[2:]:
                # further points should also be on this vertical
                if x != x0:
                    return False
            return True
        # Calculate the slope of the line passing through the first two points
        slope = (y1 - y0) / (x1 - x0) 

        for x, y in coordinates[2:]:
            # Handle vertical lines for subsequent points
            # same for verticals
            if x - x0 == 0:
                if x != x1:
                    return False
            else:
                # Check if the slope between the current point and the first point 
                # is the same as the slope of the line defined by the first two points
                if (y - y0) / (x - x0) != slope:
                    return False
        return True



    #     x1, y1 = coordinates[0]
    #     x2, y2 = coordinates[1]
    #     if x2 - x1 == 0: 
    # # Handle vertical lines
    #     for x, y in coordinates[2:]:
    #     if x != x1:
    #         return False
    #     else:
    #         slope = (y2 - y1) / (x2 - x1) 
    #         for x, y in coordinates[2:]:
    #         # Check if the slope between the current point and the first point 
    #         # is the same as the slope of the line defined by the first two points
    #         if (y - y1) / (x - x1) != slope:
    #             return False

    #     return True