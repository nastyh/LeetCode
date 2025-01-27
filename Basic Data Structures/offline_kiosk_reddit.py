"""
Reddit is so successful online, that it has decided to open an offline kiosk for people to get their physical
front page of the internet - now we just need to decide where to build it. Fortunately we have already located
the perfect city to put our first test kiosk, and like all cities, it happens to be a perfect grid.
We also happen to know the locations of all of our happy customers as intersections on the grid.
Given this customer data, what is the best place to put our kiosk?

Here is an ascii grid demonstrating this problem. Streets are lines, and locations of customers are smiley faces.
The asterisk is an example place for a kiosk on the grid.

   0  1  2  3  4  5  6  7  8
  0+--+--+--+--+--+--+--+--+
   |  |  |  |  |  |  |  |  |
  1+--+--+--+--+--+--+--+--+
   |  |  |  |  |  |  |  |  |
  2+--+--☻--+--+--+--+--☻--+
   |  |  |  |  |  |  |  |  |
  3+--+--+--+--☻--+--+--+--+
   |  |  |  |  |  |  |  |  |
  4+--+--+--+--+-[*]-+--+--+
   |  |  |  |  |  |  |  |  |
  5+--+--+--☻--+--+--+--+--+
   |  |  |  |  |  |  |  |  |
  6+--+--+--+--+--+--+--+--+
   |  |  |  |  |  |  |  |  |
  7+--+--☻--+--+--+--+--+--+
   |  |  |  |  |  |  |  |  |
  8+--+--+--+--+--+--+--+--+
Input 1 (locations):
{(2,2), (7,2), (4,3), (3,5), (2,7)}

Output 1 (any optimal location):
(3,3)

Input 2 (locations):
[(2, 2), (7, 2), (3, 4), (3, 5), (2, 7)]
Output 2 (any optimal location):
(4,3)
Note: there might be more than one optimal solutions, your program can return any one of them.

"""
from collections import Counter

def find_kiosk_location_brute_force(locations):
    """
    O(n) both
    iterate through the dictionaries to find the x and y coordinates
    with the highest counts, storing them in best_x and best_y.


    """
    x_coords = [x for x, y in locations]
    y_coords = [y for x, y in locations]

    x_counts = {}
    for x in x_coords:
        x_counts[x] = x_counts.get(x, 0) + 1

    y_counts = {}
    for y in y_coords:
        y_counts[y] = y_counts.get(y, 0) + 1

    # iterate over dicts to find the most common items
    best_x = None
    max_x_count = 0
    for x, count in x_counts.items():
        if count > max_x_count:
            best_x = x
            max_x_count = count

    best_y = None
    max_y_count = 0
    for y, count in y_counts.items():
        if count > max_y_count:
            best_y = y
            max_y_count = count
    return (best_x, best_y)


def find_kiosk_location_pythonic(locations):
    """
    O(n)
    O(n) coordinates list
    Finds an optimal location for a kiosk based on customer locations.
    Args:
        locations: A set or list of tuples representing customer (x, y) coordinates.
    Returns:
        A tuple representing the (x, y) coordinates of an optimal kiosk location.
    """

    x_coords = [x for x, y in locations]
    y_coords = [y for x, y in locations]

    x_counts = Counter(x_coords)
    y_counts = Counter(y_coords)

    best_x = x_counts.most_common(1)[0][0]  # Most frequent x-coordinate
    best_y = y_counts.most_common(1)[0][0]  # Most frequent y-coordinate

    return (best_x, best_y)


# Example usage (Input 1):
locations1 = {(2, 2), (7, 2), (4, 3), (3, 5), (2, 7)}
output1 = find_kiosk_location_brute_force(locations1)
print(f"Input 1: {locations1}")
print(f"Output 1: {output1}")



# Example usage (Input 2):
locations2 = [(2, 2), (7, 2), (3, 4), (3, 5), (2, 7)]
output2 = find_kiosk_location_pythonic(locations2)
print(f"Input 2: {locations2}")
print(f"Output 2: {output2}")



#Complexity Analysis

#Time Complexity:
#1. Extracting x and y coordinates: O(n) where n is the number of customers.
#2. Counting x and y coordinates using Counter: O(n) in the worst case (if all coordinates are unique).
#3. Finding the most common x and y coordinates: O(k) where k is the number of unique coordinates (in practice, often much smaller than n). In the worst case (all coordinates unique), k can be n.
#Overall Time Complexity: O(n) as it is dominated by the initial steps.

#Space Complexity:
#1. Storing x and y coordinates lists: O(n).
#2. Counter objects: O(k) where k is the number of unique coordinates. In the worst case (all coordinates unique), k can be n.
#Overall Space Complexity: O(n) as it is dominated by storing the coordinate lists.