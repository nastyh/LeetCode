from collections import defaultdict
def possibleBipartition(N, dislikes):  # O (N+E) both where E is the length of dislikes
    graph = defaultdict(list)
    for u, v in dislikes:
        graph[u].append(v)
        graph[v].append(u)
    color = {}
    def dfs(node, c = 0):
        if node in color:
            return color[node] == c
        color[node] = c
        return all(dfs(nei, c ^ 1) for nei in graph[node])

    return all(dfs(node)
                for node in range(1, N+1)
                if node not in color)


def possibleBipartition_bfs(N, dislikes):
    if N < 1 or not dislikes:
        return True
    
    # Transfer LC886 node pair list to LC785 graph list
    graph = {}
    for node1, node2 in dislikes:
        if node1 not in graph: graph[node1] = []
        if node2 not in graph: graph[node2] = []
        
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    dic = {}
    for graph_node in graph.keys():
        if graph_node not in dic:
            queue = [(graph_node, 0)]
            dic[graph_node] = 0
            while queue:
                queue_node, flag = queue.pop(0)
                tmp_flag = (flag + 1) % 2
                for edge in graph[queue_node]:
                    if edge in dic:
                        if dic[edge] != tmp_flag:
                            return False
                    else:
                        queue.append((edge, tmp_flag))
                        dic[edge] = tmp_flag  
    return True