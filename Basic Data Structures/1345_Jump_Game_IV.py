def minJumps(arr):  # O(n) and O(n)
    """
    search from both ends, pick the smaller end in each iteration
    """
    maps = collections.defaultdict(list)
    [maps[a].append(i) for i, a in enumerate(arr)]

    begins = set([0])
    ends = set([len(arr) - 1])
    visitedIdx = set([-1, len(arr)])
    for steps in range(len(arr)):
        if len(begins) > len(ends):
            begins, ends = ends, begins
        nextLevels = set()
        for b in begins:
            if b in ends:
                return steps
            if b in visitedIdx:
                continue
            visitedIdx.add(b)
            nextLevels.update([b - 1, b + 1] + maps[arr[b]])
            maps.pop(arr[b], None)
        begins = nextLevels


def minJumps_alt(arr):  # O(n) and O(n)
    """
    compute the layer from the end, which may be short and takes less time.
    """
    n = len(arr)
    if n <= 1:
        return 0
    graph = {}
    for i in range(n):
        if arr[i] in graph:
            graph[arr[i]].append(i)
        else:
            graph[arr[i]] = [i]
    curs = [0]  # store layers from start
    visited = {0, n - 1}
    step = 0
    other = [n - 1] # store layers from end
    # when current layer exists
    while curs:
        # search from the side with fewer nodes
        if len(curs) > len(other):
            curs, other = other, curs
        nex = []
        # iterate the layer
        for node in curs:

            # check same value
            for child in graph[arr[node]]:
                if child in other:
                    return step + 1
                if child not in visited:
                    visited.add(child)
                    nex.append(child)
            # clear the list to prevent redundant search
            graph[arr[node]].clear()
            # check neighbors
            for child in [node - 1, node + 1]:
                if child in other:
                    return step + 1
                if 0 <= child < len(arr) and child not in visited:
                    visited.add(child)
                    nex.append(child)
        curs = nex
        step += 1
    return -1