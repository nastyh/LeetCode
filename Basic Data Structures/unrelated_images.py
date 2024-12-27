"""
Given a list of pair of "unrelated images", we need to know whether we can divide the images into two groups
such that no two unrelated images are in the same group.

Case 1
I_1 <-> I_4
I_4 <-> I_8
I_8 <-> I_2

Result:
Group 1 -> [I_1, I_8]
Group 2 -> [I_4, I_2]

Case 2
I_1 <-> I_4
I_4 <-> I_8
I_8 <-> I_1
result: null
"""

from collections import defaultdict, deque

def divide_images(pairs):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for img1, img2 in pairs:
        graph[img1].append(img2)
        graph[img2].append(img1)
    # Step 2: Initialize coloring map
    color = {}
    # Step 3: Check bipartiteness using BFS
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0  # Assign the first color (0)
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        # Assign opposite color to the neighbor
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        # Conflict in coloring -> Not bipartite
                        return None
    # Step 4: Divide nodes into two groups based on color
    group1 = [node for node in color if color[node] == 0]
    group2 = [node for node in color if color[node] == 1]
    return group1, group2