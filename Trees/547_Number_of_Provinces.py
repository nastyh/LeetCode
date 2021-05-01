import numpy as np
from collections import defaultdict, deque
def findCircleNum_DFS(M):
    """
    Key here is to properly build an adjacency list w/o adding elements that are on the main diagonal
    After that, it's a traditional DFS with a helper function 
    """
    adj_list = defaultdict(list)
    visited = set()
    res = 0
    for row in range(len(M)):
        for col in range(len(M[0])):
            if M[row][col] == 1 and row != col:
                adj_list[row].append(col)
                adj_list[col].append(row)
    def _trav(node, d):
        nonlocal visited
        for neighbor in d[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                _trav(neighbor, d)
    for element in range(len(M)):
        if element not in visited:
            _trav(element, adj_list)
            res += 1
    return res
    

def findCircleNum(isConnected):  # O(n^2) to traverse the matrix and build an adj_list. O(n^2) for storage. Worst case: all nodes are connected
    """
    DFS approach
    Build an adj list. Don't include elements on the main diagonal
    Helper takes vertex as a parameter, adds it to visited, and calls itself on its neighbors.  
    We will pass the dictionary's keys in a for loop
    Every time we call the helper function on a key that we haven't seen we need to increment res
    """
    adj_list = {i : [] for i in range(len(isConnected))}
    for row in range(len(isConnected)):
        for col in range(len(isConnected[0])):
            if row != col and isConnected[row][col] == 1:
                adj_list[col].append(row)
    visited = set()
    res = 0
    def _helper(vertex):
        if vertex not in visited:
            visited.add(vertex)
            for neigh in adj_list[vertex]:
                _helper(neigh)
    for k in adj_list.keys():
        if k not in visited:
            _helper(k)
            res += 1
    return res


def find_aggregrate_metrics_bfs(isConnected):  # O(n^2) both
    """
    Again build an adj_list A.
    Add elements from it to the deque and process
    """
    N = len(isConnected)
        if N < 2: 
            return N
    A = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if isConnected[i][j] == 1 and i != j: 
                A[i].append(j)
    res = 0
    seen = set()
    for s in range(N):
        if s not in seen: 
            queue = deque([s])
            seen.add(s)
            while queue:
                s = queue.popleft()
                friends = A[s]
                for nei in friends:
                    if nei not in seen: 
                        seen.add(nei)
                        queue.append(nei)
            res += 1
    return res


def find_aggregrate_metrics_math(isConnected):
    """
    number of connected components of the matrix M (with n rows/cols). Let D be the degree matrix aka the rowsums of M, and the laplacian matrix be L = D - M.
    Then the number of connected components of M is given by the dimension of the nullspace of L. By rank-nullity, this is equal to n - rank(L). 
    """
    return len(M) - np.linalg.matrix_rank(np.diag(np.sum(isConnected, axis=1)) - np.array(isConnected))
        

if __name__ == '__main__': 
    print(findCircleNum([[1, 1, 0],[1, 1, 0],[0, 0, 1]]))
    print(findCircleNum([[1, 0, 0],[0, 1, 0],[0, 0, 1]]))
    print(findCircleNum([[1, 0, 0, 1],[0, 1, 1, 0],[0, 1, 1, 1],[1, 0, 1, 1]]))