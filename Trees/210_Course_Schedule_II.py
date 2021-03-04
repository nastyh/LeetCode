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


def task_schedule(tasks):  # from FB, if tasks are letters, not numbers
    adj_list = defaultdict(list)
    unique_tasks = set()
    for task in tasks:
        for element in task:
            unique_tasks.add(element) # (a, b, c, d, e, f)
    task_depth = {i : 0 for i in unique_tasks} # {a: 0, b: 0, c: 0, d: 0, e: 0, f: 0}
    res = []
    for task in tasks:
        adj_list[task[0]].append(task[1])  # {a: [b], c: [b], b: [d], e: [f] } 
        task_depth[task[1]] += 1  # marking tasks I can do after a given task  a: 0, b: 0, c: 0, d: 0, e: 0, f: 0}
    d = deque()
    for k in task_depth:
        if task_depth[k] == 0:
            d.append(k)
    while d:
        t = d.popleft()
        res.append(t)
        for child in adj_list[t]:
            task_depth[child] -= 1
            if task_depth[child] == 0:
                d.append(child)
    return res if len(res) == len(unique_tasks) else []


if __name__ == '__main__':
    print(findOrder(2, [[1, 0]]))
    print(findOrder(4, [[1, 0],[2, 0],[3, 1],[3, 2]]))
    print(findOrder(1, []))
    print(task_schedule([['b', 'a'], ['b', 'c'], ['d', 'b'], ['f', 'e']]))