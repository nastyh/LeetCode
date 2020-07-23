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
    return res


if __name__ == '__main__':
    print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))