from collections import deque
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    def cloneGraph(self, node):
        if not node:
            return node
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}
        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])
        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]


    def cloneGraph_recur(self, node):
        if not node: return node  
        cur_val = node.val
        if cur_val in self.new_nodes:
            return self.new_nodes[cur_val]
        cloned_node = Node(cur_val)
        self.new_nodes[cur_val] = cloned_node
        for nei in node.neighbors:
            if nei.val in self.new_nodes:
                self.new_nodes[cur_val].neighbors.append(self.new_nodes[nei.val])
            else:
                cloned_child = self.cloneGraph_recur(nei)
                self.new_nodes[cur_val].neighbors.append(cloned_child)
        
        return self.new_nodes[cur_val]


    def cloneGraph_dict(self, node):
        def dfs(map, node):
            if node is None:
                return None
            if node.val in map:
                return map[node.val]
            newNode = Node(node.val, [])
            map[node.val] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(map, neighbor))
            return newNode
        d = {}
        return dfs(d, node)