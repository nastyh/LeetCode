from collections import deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        """O(n) to iterate over n elements in favorite
        Then there is another loop for the deque and the third
        for finding cycles but still we get to O(n)
        O(n) for in_degree, depth, so overall same 

        process nodes in topological order to remove non-cycle nodes and focus on the cycles that need further examination
        begin by calculating the in-degree for each node.
        The in-degree of a node indicates how many nodes point to it.
        In this case, the "favorite" relationship can be seen as a directed edge from one person to another.
        After populating the in-degree array, we initialize a queue that will help us with the topological sort.
        The queue initially contains all nodes that have an in-degree of zero (i.e., nodes with no incoming edges).
        These are the nodes that do not form part of any cycle and can be processed in topological order
        start the process of topologically sorting the nodes while calculating the depth of each node.
        The depth represents the longest path from any starting node to that particular node.
        As we process each node, we decrement the in-degree of its neighbor (as we "remove" the edge),
        and if any neighbor's in-degree becomes zero, it is added to the queue.
        During this process, we also update the depth of each node, ensuring that
        it reflects the longest path leading to that node.
        move on to detect cycles. For each node that remains in the graph
        (i.e., nodes with a non-zero in-degree), we trace the cycle by following the favorite links.
        As we trace the cycle, we mark the nodes as visited by setting their in-degree to zero, and count the length of the cycle.
        If the cycle length is 2, we know it’s a two-person mutual favorite cycle. In this case, we add the combined depths of both nodes
        in the cycle to the total invitation count for two-cycles. This is because both nodes can invite the maximum number of people based on their depths.
        For longer cycles, we simply update the longest cycle length, since a longer cycle can accommodate more people in the seating arrangement.
        the result is the maximum of the longest cycle length and the total size of the two-cycle groups.
        """
        if len(favorite) == 2: return 2  # edge case from the q
        n = len(favorite)
        d = deque()
        in_degree = [0] * n
        for person in range(n):
            in_degree[favorite[person]] += 1 # how many people like a given person 
        for person in range(n):
            if in_degree[person] == 0: # nobody likes this person, no cycle
                d.append(person)
        depth = [1] * n  # Depth of each node
        while d:
            current_node = d.popleft()
            next_node = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                d.append(next_node)

        longest_cycle = 0
        two_cycle_invitations = 0

        # Detect cycles
        for person in range(n):
            if in_degree[person] == 0:  # Already processed
                continue

            cycle_length = 0
            current = person
            while in_degree[current] != 0:
                in_degree[current] = 0  # Mark as visited
                cycle_length += 1
                current = favorite[current]

            if cycle_length == 2:
                # For 2-cycles, add the depth of both nodes
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, two_cycle_invitations)
