from collections import defaultdict
def makeConnected(n, connections):  # O(V + E) both 
    """
    Idea is to count the number of disconnected islands and return this number minus 1
    Edge case: if len(connections) < n - 1: return -1
    Create a normal adj_list
    _helper does DFS: it only visits neighbors and adds everything to visited
    Then this helper is called on everything in range(n)
    If there are disconnected components, the loop will run more than once, it's tracked by res
    """
    adj_list = defaultdict(list)
    visited = set()
    res = 0
    if len(connections) < n - 1: return -1
    for connection in connections:
        adj_list[connection[0]].append(connection[1])
        adj_list[connection[1]].append(connection[0])
    def _helper(node, visited):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                _helper(neighbor, visited)
    for i in range(n):
        if i not in visited:
            _helper(i, visited)
            res += 1
    return res - 1
