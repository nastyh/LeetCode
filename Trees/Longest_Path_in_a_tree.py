"""
Given the following classes:

class Node {
	int id;
	Link[] links;
}

class Link {
	int bytesPerSec;
	Node dest;
}

Imagine you have a graph of nodes and links find the time it takes to get information from a root node to all the other nodes.

int time(Node root) {
	// todo
}

"""

from collections import defaultdict
from heapq import heappush, heappop
class Node:
    def __init__(self, val = None, links = []):
        self.val = val
        self.links = links # list of adjacent nodes with edge weights
    
    def __lt__(self, other):
        return self.val < other.val
        
class Link:
    def __init__(self, bytesPerSec = None, destNode = None):
        self.bytesPerSec = bytesPerSec
        self.destNode = destNode
    
def dijkstra(sourceNode, databytes, N):
    # do stuff here
    dist = defaultdict(lambda : float('inf'))
    dist[sourceNode.val] = 0
    q = []
    heappush(q, (0,sourceNode, sourceNode.val))
    visited = set()
    
    while q:
        distance, node, val = heappop(q)
        visited.add(node.val)
        path.append(node.val)   
        
        for neighbor in node.links:
            bytesPerSec = neighbor.bytesPerSec
            destNode = neighbor.destNode
            x = dist[destNode.val]
            y = dist[node.val]
            w =  y + databytes / bytesPerSec
            if not destNode.val in visited and x > w:
                dist[destNode.val] = w
                heappush(q, (w, destNode, destNode.val))
    ans = max(dist.values())
    # print(len(dist))
    # print(dist)
    return ans if len(dist) == N else -1
    

# Solution for an N-ary tree

class Node
    def __init__(self, val = None, links = []):
        self.val = val
        self.links = links # list of adjacent nodes with edge weights
        
class Link:
    def __init__(self, bytesPerSec = None, destNode = None):
        self.bytesPerSec = bytesPerSec
        self.destNode = destNode
    
def dfs(node, databytes, maxLength, currLength, path):
    # do stuff here
    path.append(node.val)
    if len(node.links) == 0 and currLength > maxLength[0]:
        maxLength[0] = currLength
    
    print(node.val, maxLength, currLength, len(node.links))
    
    if not node.links:
        return
    for neighbor in node.links:
        weight = neighbor.bytesPerSec
        destNode = neighbor.destNode
        dfs(destNode, databytes, maxLength, currLength + databytes/weight, path)


if __name__ == '__main__':
    nodeF = Node('F')
    nodeH = Node('H', [Link(2, nodeF)])
    nodeC = Node('C', [Link(1, nodeH)])
    nodeG = Node('G', [Link(1, nodeC)])
    nodeE = Node('E')

    nodeB = Node('B', [Link(5, nodeF), Link(4, nodeG)])
    nodeD = Node('D', [Link(3, nodeH), Link(1, nodeE)])
    nodeA = Node('A', [Link(2, nodeB), Link(3, nodeC), Link(2, nodeD), Link(4, nodeE)])

    maxLength = [float('-inf')]
    path = []
    dataBytes = 12 # info to send from source to all other nodes of the graph
    N = 8 # no. of nodes in graph
    ans = dijkstra(nodeA, dataBytes, N)
    print('Length of longest path (max time for info to reach to all nodes):', ans)

    # let's try for a graph in which info won't reach to a node X
    nodeE = Node('X', [Link(3, nodeE)])
    res = dijkstra(nodeA, dataBytes, N = 9)
    print('Length of longest path (max time for info to reach to all nodes):', res)