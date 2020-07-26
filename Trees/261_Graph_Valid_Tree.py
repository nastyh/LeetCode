from collections import defaultdict
def validTree(n, edges):
    def detect_cycle(node, visited, parent):
        visited.add(node)
        for child in graph[node]:
            if(child == parent): continue
            if(child in visited or detect_cycle(child, visited, node)):        
                return True
        return False       

    if(n <= 0 or len(edges) != n - 1): return False
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)              
        graph[v].append(u)           
    visited = set()
    if(detect_cycle(0, visited, -1)):      
        return False                       
    return len(visited) == n    


if __name__ == '__main__':
    print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))