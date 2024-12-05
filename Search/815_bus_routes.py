class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        O(mn) both where number of buses and number of stops respectively 

        Adj list needs to have a list of unique bus stops and what buses serve them
        Need sets in order to avoid loops 
        Then a normal BFS (topological sort)
        """
        if source == target: return 0
        adj_l, res = defaultdict(list), 0
        visited_stops, visited_buses, d = set(), set(), deque()
        visited_stops.add(source)
        d.append(source)

        for bus, route in enumerate(routes):
            """
            adj_list has a shape of stop: [indices of buses that serve this stop]
            """
            for stop in route:
                adj_l[stop].append(bus)
        if source not in adj_l: return -1
        while d:
            len_d = len(d)
            for _ in range(len_d):
                curr_stop = d.popleft()
                if curr_stop == target:
                    return res 
                for bus in adj_l[curr_stop]:
                    if bus not in visited_buses:
                        for stop in routes[bus]:
                            if stop not in visited_stops:
                                visited_stops.add(stop)
                                d.append(stop)
                        visited_buses.add(bus)
            res += 1
        return -1