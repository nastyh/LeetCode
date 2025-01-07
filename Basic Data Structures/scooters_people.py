"""
write a function or method or subprogram that, given a person and a scooter map, returns
the best scooter for that person to head for to minimize their pre-scooter walking. I’ll give every person
on the map a copy of your program, and they'll all run it at the same time.

I'll provide the program with a map of the neighborhood as a string containing newline separated rows, all
of the same length, with an “x” to mark an empty spot on the map, an “s” to mark every spot where there is
a scooter, and a “p” to mark every spot where there is a person who wants a scooter.

Here's a map now

xxpxxxs
xsxxxxx
xxxxxpx

In this map there are two people and two scooters. The result of the function should return:

- the person at row: 0, column: 2 (0, 2) is two steps away from the scooter at row: 1, column: 1 (1,1)
- the person at row: 2, column: 5 (2, 5) is three steps away from the scooter at row: 0, column: 6 (0, 6)
"""
def findScooters(map_str):
    """
    O(rows*cols) to go over everything
    O(scooters + people) to save the res
    Assign each person their nearest available scooter, ensuring no two people
    are assigned the same scooter and respecting the order of the input map.
    """
    # Parse the map into a grid
    map_rows = map_str.strip().split("\n")  # optional 
    persons = []
    scooters = []
    # Locate all persons ('p') and scooters ('s') on the map
    for r, row in enumerate(map_rows):
        for c, cell in enumerate(row):
            if cell == 'p':
                persons.append((r, c))
            elif cell == 's':
                scooters.append((r, c))

    # Function to calculate Manhattan distance
    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    # Assign scooters to persons
    assignments = {}
    used_scooters = set()
    for person in persons:
        # Find the nearest available scooter
        nearest_scooter = None
        nearest_distance = float('inf')
        for scooter in scooters:
            """
            just local and glob min
            """
            if scooter not in used_scooters:
                distance = manhattan_distance(person, scooter)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_scooter = scooter

        # Assign the person to the nearest scooter and mark it as used
        if nearest_scooter:
            assignments[person] = nearest_scooter
            used_scooters.add(nearest_scooter)

    return assignments

    def findScooters_heap(map_str):
        """
        O(PSlog(PS)), persons and scooters
        O(P+S)
        """
        persons = []
        scooters = []

        # Locate all persons ('p') and scooters ('s') on the map
        for r, row in enumerate(map_rows):
            for c, cell in enumerate(row):
                if cell == 'p':
                    persons.append((r, c))
                elif cell == 's':
                    scooters.append((r, c))

        # Function to calculate Manhattan distance
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Create a priority queue for all person-scooter pairs
        pq = []
        for person in persons:
            for scooter in scooters:
                distance = manhattan_distance(person, scooter)
                heapq.heappush(pq, (distance, person, scooter))

        # Assign scooters to persons greedily based on minimum distance
        assignments = {}
        used_scooters = set()

        while pq and len(assignments) < len(persons):
            distance, person, scooter = heapq.heappop(pq)
            if person not in assignments and scooter not in used_scooters:
                assignments[person] = scooter
                used_scooters.add(scooter)

        return assignments


# Example map
map2 = [
    'xxxxxxxxpx',
    'xxxxxxxpxx',
    'xxxxxxpxxx',
    'xxxsxxxxxx',
    'xxsxxxxxxx',
    'xsxxxxxxxx'
]

# Convert to string for function input
map_str = "\n".join(map2)

# Run the function
assignments = findScooters(map_str)

# Display results
print(assignments)


