from collections import defaultdict
def validTree(n, edges):
    if n <= 0 or len(edges) != n - 1: 
        return False 
    adj_l = defaultdict(list)
    for el_ix in range(len(edges)):
        adj_l[edges[el_ix][0]].append(edges[el_ix][1])
        adj_l[edges[el_ix][1]].append(edges[el_ix][0])
    visited = set()

    def _helper(node, visited, parent):
        visited.add(node)
        for n in adj_l[node]:
            if n == parent:
                continue
            if (n in visited or _helper(n, visited, parent)):
                return True
        return False

    if _helper(0, visited, -1):
        return False
    return len(visited) == n


if __name__ == '__main__':
    print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))