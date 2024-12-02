from collections import deque

def find_compilation_order(dependencies):
    """
    [[A, B], [B, C], [C, D]]
    means in order to run A, you need to run B first
    In order to run B, you need to run C first
    In order to run C, you need to run D first 
    So the order will be D, C, B, A
    """
    adj_list = defaultdict(list)
    degrees_count = {}
    res = []
    for dep in dependencies:
        degrees_count[dep[1]] = 0
        degrees_count[dep[0]] = 0
    for dep in dependencies:
        adj_list[dep[1]].append(dep[0])
        degrees_count[dep[0]] += 1
    # degrees count with 0 means elements that don't need prerequisites 
    d = deque()
    for k, v in degrees_count.items():
        if v == 0:
            d.append(k)

    while d: 
        t = d.popleft()
        res.append(t)
        for child in adj_list[t]:
            degrees_count[child] -= 1
            if degrees_count[child] == 0:
                d.append(child)
    if len(res) != len(adj_list):
        return []
    return res 

