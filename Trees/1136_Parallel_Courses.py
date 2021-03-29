from collections import defaultdict, deque
def minimumSemesters_bfs(N, relations):  # O(N + E) both 
    """
    Topological sorting: need to have an in_degree list in order to know from what class to start
    Then BFS with decrementing in_degree and adding elements back for processing 
    """
    res, d, studied_class = 0, deque(), 0
    adj_list = defaultdict(list)
    in_degree = {i: 0 for i in range(1, N + 1)}
    for relation in relations:
        adj_list[relation[0]].append(relation[1])
        in_degree[relation[1]] += 1
    d = deque()
    for k, v in in_degree.items():
        if v == 0:
            d.append(k)
    while d:
        res += 1
        next_d = []
        for node in d:
            studied_class += 1
            ending_nodes = adj_list[node]
            for end_n in ending_nodes:
                in_degree[end_n] -= 1
                if in_degree[end_n] == 0:
                    next_d.append(end_n)
        d = next_d
    return res if studied_class == N else -1


def minimumSemesters_dfs(N, relations):
    dependences = defaultdict(list)  # course and its dependences
	for a, b in relations:
		dependences[b].append(a)
    node_depth = {}

    def visit(node):
		if node in node_depth: return node_depth[node]
		node_depth[node] = -1  # visiting
		maxdep = 0
		for dep in dependences[node]:
			depth = visit(dep)
			if depth == -1: return -1
			maxdep = max(maxdep, depth)
		del dependences[node]
		node_depth[node] = 1 + maxdep
		return node_depth[node]

    while dependences:
		if visit(next(iter(dependences))) == -1: return -1
	return max(node_depth.values())
    

def minimumSemesters(N, relations):
    courseTaken, semesterCount = [], 0
    # a. initialise the graph
    inDegree = {}
    graph = {}
    for i in range(1, N + 1):
        inDegree[i] = 0
        graph[i] = []
    # b. build graph
    for relation in relations:
        courseX, courseY = relation[0], relation[1]
        graph[courseX].append(courseY)
        inDegree[courseY] += 1
    # c. find all sources. all vertices with 0 inDegree
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)
    # d. check for cycle. If we don't have any source course to start then there is a cycle and we are not ale to finish the courses
    courseCountForThisSemester = 0
    if len(sources) > 0:
        semesterCount += 1
        courseCountForThisSemester = len(sources)
    else:
        return -1
    # d. For each source, add it to the courseTaken and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        if courseCountForThisSemester <= 0: # We have taken all the course of this semester
            semesterCount += 1          # Start of a new semester
            courseCountForThisSemester = len(sources)  # Course we can take o the new semester that we are going to start
        courseCountForThisSemester -= 1  # take a course on this semester
        vertex = sources.popleft()
        courseTaken.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
    if len(courseTaken) != N: # We were not able to take all the course because of a cyclic dependency
        return -1
    return semesterCount