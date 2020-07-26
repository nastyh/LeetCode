from collections import defaultdict
def countComponents(n, edges):
    adj_l = defaultdict(list)
    for el_ix in range(len(edges)):
        adj_l[edges[el_ix][0]].append(edges[el_ix][1])
        adj_l[edges[el_ix][1]].append(edges[el_ix][0])
    def _helper(node, visited):
        visited.add(node)
        for n in adj_l[node]:
            if n not in visited:
                _helper(n, visited)
    res, visited = 0, set()
    for el in range(n):
        if el not in visited:
            _helper(el, visited)
            res += 1
    return res, len(visited) == n

def countComponents_another(n, edges): # instead of a set, have an extra dictionary with values == 0 while respective keys (nodes) aren't visited
    d = defaultdict(list)
    res = 0
    for e in range(len(edges)):
        d[edges[e][0]].append(edges[e][1])
        d[edges[e][1]].append(edges[e][0])
    flags = {k:0 for k in d.keys()}
    def _helper(node, f):
        f[node] = 1
        for els in d[node]:
            if f[els] == 0:
                _helper(els, f)
    for el in range(n):
        try: 
            if flags[el] == 0:
                _helper(el, flags)
                res += 1
        except KeyError:
            flags[el] = 0
            res += 1
    return res

if __name__ == '__main__':
    print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))
    # print(countComponents_another(5, [[0, 1], [1, 2], [3, 4]]))
    print(countComponents_another(4, [[2, 3], [1, 2], [1, 3]]))
    print(countComponents_another(5, [[0, 1], [1, 2], [3, 4]]))