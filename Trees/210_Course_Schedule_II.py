from collections import deque, defaultdict
def findOrder(numCourses, prerequisites):  # O(V + E) both, where V is the number of vertices and E are edges
    adj_list = defaultdict(list)
    degree_count = {i : 0 for i in range(numCourses)}
    res = []
    for el in prerequisites:
        take_second = el[0]  
        take_first = el[1] 
        adj_list[take_first].append(take_second)  
        degree_count[take_second] += 1  # marking children 
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
    return res if len(res) == numCourses else []  # if there is a cycle, we need to return an empty list 


if __name__ == '__main__':
    print(findOrder(2, [[1, 0]]))
    print(findOrder(4, [[1, 0],[2, 0],[3, 1],[3, 2]]))
    print(findOrder(1, []))