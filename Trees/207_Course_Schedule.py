def dfs(nd,vis):
        if vis[nd]==1:
            return True
        if vis[nd]==2:
            return False
        vis[nd]=1
        for m in dc[nd]:
            if vis[m]!=2 and dfs(m,vis):
                return True
        vis[nd]=2
        return False

    dc=collections.defaultdict(list)

    for a,b in pr:
        dc[b].append(a)

    vis=[0]*nc
    for nd in range(nc):
        if dfs(nd,vis):
            return False

    return True


from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #BFS
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
