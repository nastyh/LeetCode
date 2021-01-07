from collections import deque, defaultdict
def canFinish(numCourses, prerequisites):  # O(E + V) both where V is the number of courses and E is the number of dependencies 
    """
    This is topological sort
    Need a usual adj_list (but in one direction)
    Need a dictionary degree_count that will contain vertices that have never been children
    Put that vertex into a deque and start iterating over its children. 
    Decrease the count for this children in degree_count. Once it's zero, add this element to the deque
    If you can traverse the whole graph, it means there is no cycle, thus, return True
    """
    adj_list = defaultdict(list)
    degree_count = {i : 0 for i in range(numCourses)}
    res = []
    for el in prerequisites:
        st = el[0]  # parent
        fin = el[1]  # child
        adj_list[st].append(fin)  # building a normal adjacency list
        degree_count[fin] += 1  # marking children 
    sources = deque()
    for k in degree_count:  # adding vertices that have never been children to the deque. List comprehension doesn't work here for some reason
        if degree_count[k] == 0:
            sources.append(k)
    while sources:
        t = sources.popleft()
        res.append(t)
        for child in adj_list[t]:
            degree_count[child] -= 1
            if degree_count[child] == 0:
                sources.append(child)
    return len(res) == numCourses


def dfs(nd, vis):
    if vis[nd] == 1:
        return True
    if vis[nd] == 2:
        return False
    vis[nd] = 1
    for m in dc[nd]:
        if vis[m] != 2 and dfs(m,vis):
            return True
    vis[nd] = 2
    return False

    dc=collections.defaultdict(list)
    for a,b in pr:
        dc[b].append(a)
    vis=[0]*nc
    for nd in range(nc):
        if dfs(nd,vis):
            return False
    return True

def canFinish_alt(numCourses, prerequisites):
    #another interpretation of the topological sort 
    edges = [[] for i in range(numCourses)]
    inDegree = [0 for i in range(numCourses)]

    for edge in prerequisites:
        inDegree[edge[0]] += 1
        edges[edge[1]].append(edge[0])

    q, count = deque(), 0

    for node in range(numCourses):
        if inDegree[node] == 0:
            q.append(node)

    while q:
        node = q.popleft()
        count += 1
        for neigh in edges[node]:
            inDegree[neigh] -= 1
            if inDegree[neigh] == 0:
                q.append(neigh)
    return count == numCourses


if __name__ == '__main__':
    print(canFinish(3, [[0, 1], [1, 2]]))
    print(canFinish(2, [[1, 0]]))
    print(canFinish(2, [[1, 0], [0, 1]]))
