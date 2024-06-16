from collections import defaultdict
 def findItinerary_recursion_explained(self, tickets: List[List[str]]) -> List[str]:
        """
        O(E*log(E/V)), where E is the num of edges/flights and V is the num of airports. Log due to sorting
        O(∣V∣+2⋅∣E∣)=O(∣V∣+∣E∣): V + E for the graph, E if for the recursion stack, we run recursion for the number of flights 
 
        we will sort by the origin b/c of the lexical order in the task
        default dict of the shape: origin: [destinations] 
        by the lexical order (how the question wants it)

        """
        d, res = defaultdict(list), []
        for origin, dest in sorted(tickets, reverse = True): # from larger to smaller
            # in this order b/c popping happens from the end of the list and we want to process
            # airports that have a a smaller lexographic order first (smaller letter first)
            # d[sorted origins] = [all destinations]
            d[origin].append(dest)
        def _helper(d, location, res):
            if location in d and len(d[location]) > 0: 
                # means we departed from here and have somewhere to go
                while len(d[location]) > 0: # while we have somewhwere to go
                    destination = d[location].pop() # to make sure we covered this destination and then get rid of it
                    _helper(d, destination, res) # this destination becomes our departure point 
            res.append(location)  # keep building our answer: current locations goes into the list 
        _helper(d, "JFK", res) 
        # b/c based on the question, everyone departs from JFK
        return res[::-1] # b/c recursion built the answer from the end: from the airport from which we don't travel anywhere

    def findItinerary_iter(self, tickets: List[List[str]]) -> List[str]:
        d, res = defaultdict(list), []
        # same dict 
        for origin, dest in sorted(tickets, reverse = True):
            d[origin].append(dest)
        st = ["JFK"] # since everyone starts here
        while st:
            while d[st[-1]]: # while we have somewhere to go from a given airport
                st.append(d[st[-1]].pop()) # take it and process the destinations to go from this airport
            res.append(st.pop()) # build the result 
        return res[::-1]
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

