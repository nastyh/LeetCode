from collections import defaultdict
def findItinerary_DFS(tickets):  # O(E log(E/V)) and O(E+V) log is here b/c of sorting
    res = []
    def _helper(location):
        while d[location]:
            _helper(d[location].pop())
        res.append(location)
    d = defaultdict(list)
    for origin, destination in sorted(tickets, reverse = True):
        d[origin].append(destination)
    _helper("JFK")
    return res[::-1]


def findItinerary_stack(tickets):
    d = defaultdict(list)
    for origin, destination in sorted(tickets, reverse = True):
        d[origin].append(destination)
    st, res = [], []
    stop = "JFK"
    while stop:
        if not d[stop]:
            res.append(stop)
            stop = None if not st else st.pop()
        else:
            st.append(stop)
            stop = d[stop].pop()
    return res[::-1]


def findItinerary_recur(tickets):
    """
    Create adj list: origin: [destination] but destinations should be sorted 
    Then start popping destinations from the list and recursively cover them
    Addition to res happens iff we flew back and forth enough times
    """
    d = defaultdict(list)
    res = []
    for origin, destination in sorted(tickets, reverse = True):
        d[origin].append(destination)

    def _helper(d, location, res):
        if location in d and len(d[location]) > 0:
            while len(d[location]) > 0:
                destination = d[location].pop()
                _helper(d, destination, res)
        res.append(location)
    
    _helper(d, "JFK", res)
    return res[::-1]


def findItinerary_doesnt_work(tickets):
    d = defaultdict(list)
    for ticket in tickets:
        d[ticket[0]].append(ticket[1])
    if 'JFK' not in d: return []
    visited = set()
    res = ["JFK"]
    def _helper(node, d):
        nonlocal visited
        nonlocal res
        if node != "JFK":
            visited.add(node)
        for neighbor in d[res[-1]]:
            if neighbor not in visited:
                if neighbor == 'JFK': continue
                else:
                    visited.add(neighbor)
                res.append(neighbor)
                _helper(neighbor, d)
        return res
    return _helper("JFK", d)



if __name__ == '__main__': 
    print(findItinerary_DFS( [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(findItinerary_DFS( [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(findItinerary_stack( [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(findItinerary_stack( [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
    print(findItinerary_recur( [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(findItinerary_recur( [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

