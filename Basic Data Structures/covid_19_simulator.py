"""
This question is about building an Covid19 infection simulation algorithm assuming covid 19
transmits when infected users in the same location and same time as non infected users.

Given an array of visits(user_id, location_id, start_time, end_time) and an array of users
infected with Covid 19 users write a function that returns the total number of users that caught
Covid19.
When a user gets infected they will start infecting other users afterwards immediately
meaning the person becomes contagious right after being infected and there is no
incubation period.

visits = [
[0, 0, 1, 3],
[0, 1, 4, 5],
[0, 2, 8, 9],
[1, 1, 4, 6],
[2, 2, 7, 9],
[3, 2, 6, 8],
]
infected = [1]
infection_simulator(visits, infected) # returns 3
# first 1 infects 0 at location 1
# then 0 infects 2 at location 2
# 3 remains uninfected cause they leave as soon as 0
arrives at location 2 

Is end time inclusive or exclusive?
○ end_time is exclusive meaning if user1 visited location 1 from 0 to 5 and
user2(covid infected) with covid came strictly at 5 user1 won’t be infected.
● Do users recover from covid?
○ No, data collected here was over the span of a few days where users didn’t have
enough time to recover (to keep it simple).
● Can the same user be in multiple locations at same time?
○ No, a user is guaranteed to be in at most one location at any point of time.
● When users get infected can they infect other users afterwards right away?
○ Yes, unfortunately as covid 19 evolved and became spreading much faster.
"""

from collections import defaultdict
import heapq
import math


def infection_simulator(visited, infected):
    """
    O(nlogn) dominates due to sorting
    O(n) due to infection_time dict and loation_users dict
    Each visit is split into an arrival event (at start_time) and a departure event (at end_time).
    Since the end time is exclusive, departures are processed before arrivals at the same time.
    This ensures that if one user leaves at time 5 and another arrives at time 5, they do not overlap, preventing infection

    Departures: Users are removed from the current location.
    Arrivals: For all arrivals at the same time, the simulation checks if the location
    is "exposed" by either already having an infected user or by having an arriving infected user.
    If exposed, all arriving users are marked as infected (if they aren’t already).
    Once a user is infected, they immediately become contagious and can infect others in any future visits overlapping in time.
    """
    # Mark initially infected users with infection time 0.
    infection_time = {user: 0 for user in infected}
    events = []
    # Create two events for each visit: one for arrival and one for departure.
    for user, loc, start, end in visited:
        # Note: end_time is exclusive, so departures are processed before arrivals at the same time.
        events.append((start, "arrival", user, loc))
        events.append((end, "departure", user, loc))
    # Sort events: first by time; for events with the same time, departures come before arrivals.
    events.sort(key=lambda x: (x[0], 0 if x[1]=="departure" else 1))

    location_users = defaultdict(set)
    i = 0
    n = len(events)
    while i < n:
        current_time = events[i][0]
        # Process all departures at current_time.
        while i < n and events[i][0] == current_time and events[i][1] == "departure":
            _, _, user, loc = events[i]
            if user in location_users[loc]:
                location_users[loc].remove(user)
            i += 1

        # Collect all arrivals at current_time.
        batch = []
        while i < n and events[i][0] == current_time and events[i][1] == "arrival":
            batch.append(events[i])
            i += 1

        # Group arriving users by location.
        arrivals_by_loc = defaultdict(list)
        for _, _, user, loc in batch:
            arrivals_by_loc[loc].append(user)
        
        # For each location, determine if the arriving users are exposed.
        for loc, arriving_users in arrivals_by_loc.items():
            # Check if any user already present is infected (infection_time <= current_time)
            exposed = any(
                (user in infection_time and infection_time[user] <= current_time)
                for user in location_users[loc]
            )
            # Also, if any arriving user is already infected, then everyone arriving becomes infected.
            if not exposed:
                exposed = any(
                    (user in infection_time and infection_time[user] <= current_time)
                    for user in arriving_users
                )
            # If the location is exposed, infect every user arriving at this time.
            if exposed:
                for user in arriving_users:
                    if user not in infection_time:
                        infection_time[user] = current_time

            # Finally, add all arriving users to the location.
            for user in arriving_users:
                location_users[loc].add(user)
    
    # Return the total number of infected users.
    return len(infection_time)



def infection_simulator_update(visits, infected, K):
    """
    How would you change the solution if covid19 didn’t start spreading immediately but
    rather had an incubation period of K time units before being contagious.

    Store the Contagious Time:
    Instead of recording the time a user is infected as the moment they’re contagious,
    record the time when they will start infecting others. For initially infected users,
    you can assume they are already contagious (i.e., contagious time = 0).
    For a newly infected user at time t, set their contagious time to t + K.

    Adjust the Exposure Check:
    When processing events at a given time, check for “exposure” only from
    those users who are already contagious (i.e., whose contagious time is ≤ the current event time).
    In other words, even if a user gets infected in the current batch, they should not immediately infect
    others in that same batch because their contagious time is t + K, which is in the future.
    """
    # For initially infected users, assume they are already contagious.
    contagious_time = {user: 0 for user in infected}

    events = []
    # Create events for each visit: an arrival and a departure.
    for user, loc, start, end in visits:
        # end_time is exclusive, so departures are processed before arrivals at the same time.
        events.append((start, "arrival", user, loc))
        events.append((end, "departure", user, loc))
    
    # Sort events by time; departures come before arrivals at the same time.
    events.sort(key=lambda x: (x[0], 0 if x[1] == "departure" else 1))
    
    # Track which users are currently at each location.
    location_users = defaultdict(set)
    
    i = 0
    n = len(events)
    while i < n:
        current_time = events[i][0]
        # Process all departures at current_time.
        while i < n and events[i][0] == current_time and events[i][1] == "departure":
            _, _, user, loc = events[i]
            location_users[loc].discard(user)
            i += 1

        # Collect all arrivals at current_time.
        batch = []
        while i < n and events[i][0] == current_time and events[i][1] == "arrival":
            batch.append(events[i])
            i += 1

        # Group arriving users by location.
        arrivals_by_loc = defaultdict(list)
        for _, _, user, loc in batch:
            arrivals_by_loc[loc].append(user)
        
        # For each location, check if the arriving users are exposed.
        for loc, arriving_users in arrivals_by_loc.items():
            # Check if any user already present is contagious at the current time.
            exposed = any(
                user in contagious_time and contagious_time[user] <= current_time
                for user in location_users[loc]
            )
            # Also check if any arriving user is already contagious.
            if not exposed:
                exposed = any(
                    user in contagious_time and contagious_time[user] <= current_time
                    for user in arriving_users
                )
            # If the location is exposed, infect every arriving user (if not already infected).
            if exposed:
                for user in arriving_users:
                    if user not in contagious_time:
                        # Newly infected users become contagious only after the incubation period.
                        contagious_time[user] = current_time + K

            # Add all arriving users to the location.
            for user in arriving_users:
                location_users[loc].add(user)
    
    # Return the total number of infected users.
    return len(contagious_time)

def infection_simulator_update_more(visits, initial_infected, K, X, negative_tests):
    """
    How would you handle recovery if users would recover after X time from they got
    infected.
    Additional input: An array of (userid, test_time) which tells that this particular user
    has tested at this time and the test result was negative.

    visits: List of [user_id, location_id, start_time, end_time]
    initial_infected: List of initially infected user ids.
    K: Incubation period (time units after infection before a user becomes contagious).
       For example, if K = 0 then infection is immediately contagious.
    X: Recovery period (time units after infection at which the user recovers by default).
    negative_tests: List of (user_id, test_time) tuples indicating that the user tested negative
    at test_time (and thus is considered recovered from that moment).

    The negative tests are preprocessed so that for each user, you know the earliest time
    they were confirmed negative. When a user is infected, their recovery time becomes the minimum
    of the default recovery time (infection_time + X) and the negative test time if one exists.

    In every event batch, when determining if a location is “exposed,” the simulation only
    counts users as infectious if the current time is between their contagious time and their recovery time.
    That means if a user has recovered (current_time ≥ recovery_time), they won’t infect others even if they are still present.
    The event simulation (processing arrivals and departures) remains essentially the same.
    The only difference is the added check against recovery time before a user can cause a new infection.
    """
    # Preprocess negative tests to get the earliest negative test time per user.
    negative_test_time = {}
    for user, t in negative_tests:
        if user not in negative_test_time or t < negative_test_time[user]:
            negative_test_time[user] = t

    # For each infected user, store a tuple: (infection_time, contagious_time, recovery_time)
    infection_info = {}
    # For initially infected users, assume they are infected at time 0 and are already contagious.
    for user in initial_infected:
        infected_time = 0
        contagious_time = 0  # already contagious
        # Default recovery time is infection_time + X.
        rec_time = infected_time + X
        # If there is a negative test for this user, they recover at the earlier time.
        if user in negative_test_time:
            rec_time = min(rec_time, negative_test_time[user])
        infection_info[user] = (infected_time, contagious_time, rec_time)

    # Create arrival and departure events.
    events = []
    for user, loc, start, end in visits:
        # Note: end time is exclusive so departures are processed before arrivals at the same time.
        events.append((start, "arrival", user, loc))
        events.append((end, "departure", user, loc))
    events.sort(key=lambda x: (x[0], 0 if x[1]=="departure" else 1))
    
    # Track users currently present at each location.
    location_users = defaultdict(set)
    i = 0
    n = len(events)
    while i < n:
        current_time = events[i][0]
        # Process all departures at current_time.
        while i < n and events[i][0] == current_time and events[i][1] == "departure":
            _, _, user, loc = events[i]
            location_users[loc].discard(user)
            i += 1
        
        # Process all arrivals at current_time.
        batch = []
        while i < n and events[i][0] == current_time and events[i][1] == "arrival":
            batch.append(events[i])
            i += 1

        # Group arrivals by location.
        arrivals_by_loc = defaultdict(list)
        for _, _, user, loc in batch:
            arrivals_by_loc[loc].append(user)

        # For each location, check if there is any infectious user (i.e. contagious and not recovered).
        for loc, arriving_users in arrivals_by_loc.items():
            exposed = any(
                user in infection_info and 
                infection_info[user][1] <= current_time < infection_info[user][2]
                for user in location_users[loc]
            )
            # Also check arriving users themselves, in case one of them is already infectious.
            if not exposed:
                exposed = any(
                    user in infection_info and 
                    infection_info[user][1] <= current_time < infection_info[user][2]
                    for user in arriving_users
                )
            # If the location is exposed, infect every arriving user who isn't already infected.
            if exposed:
                for user in arriving_users:
                    if user not in infection_info:
                        infected_time = current_time
                        # They become contagious after the incubation period K.
                        contagious_time = current_time + K
                        # Their default recovery is after X time units.
                        rec_time = infected_time + X
                        if user in negative_test_time:
                            rec_time = min(rec_time, negative_test_time[user])
                        infection_info[user] = (infected_time, contagious_time, rec_time)
            # Add the arriving users to the location.
            for user in arriving_users:
                location_users[loc].add(user)
    
    # The total number of users ever infected.
    return len(infection_info)

from collections import defaultdict
from typing import Dict, Tuple, List

class StreamingInfectionSimulator:
    """
    How would you solve the problem if data arrived in a streaming/online fashion rather
    than everything upfront?
    O(1) locations are bounded, so the average time is O(1)
    O(n) dict 
    """
    def __init__(self, initial_infected: List[int], K: int, X: int):
        """
        initial_infected: List of user ids that are infected at time 0 (assumed contagious immediately).
        K: Incubation period – time units after infection before a user becomes contagious.
        X: Recovery period – time units after infection at which the user recovers by default.
        You continuously update your mapping of which users are at which location and what their infection status is.
        This lets you decide immediately—when a new visit arrives—if the user becomes infected.
        The infection check only considers users currently present and their contagious state at the moment the event is processed.
        If events might be received out of order, a buffering strategy (with a sliding window) can ensure events are processed in nearly chronological order.
        """
        self.K = K  # incubation period
        self.X = X  # recovery period
        # infection_info maps user_id -> (infected_time, contagious_time, recovery_time)
        self.infection_info: Dict[int, Tuple[int, int, int]] = {}
        for user in initial_infected:
            # Initially infected users are set with infected_time=0, contagious_time=0, and recovery at time X.
            self.infection_info[user] = (0, 0, X)
        # location_state maps location_id -> set of users currently present.
        self.location_state = defaultdict(set)

    def process_arrival(self, time: int, user: int, location: int):
        """
        Process an arrival event at the given time for the user at the specified location.
        If any user at the location is infectious, the arriving user gets infected.
        """
        # Check for any infectious user at the location.
        exposed = False
        for other in self.location_state[location]:
            if other in self.infection_info:
                infected_time, contagious_time, recovery_time = self.infection_info[other]
                if contagious_time <= time < recovery_time:
                    exposed = True
                    break
        # Also check if the arriving user is already infectious (from a previous visit).
        if not exposed and user in self.infection_info:
            _, contagious_time, recovery_time = self.infection_info[user]
            if contagious_time <= time < recovery_time:
                exposed = True
        
        # If the user is exposed and not already infected, infect them.
        if exposed and user not in self.infection_info:
            infected_time = time
            contagious_time = time + self.K  # user becomes contagious only after the incubation period.
            recovery_time = time + self.X     # default recovery time.
            self.infection_info[user] = (infected_time, contagious_time, recovery_time)
            print(f"User {user} got infected at time {time} (contagious at {contagious_time}, recovery by {recovery_time}).")
        
        # Finally, add the arriving user to the current location.
        self.location_state[location].add(user)

    def process_departure(self, time: int, user: int, location: int):
        """Process a departure event: remove the user from the location."""
        self.location_state[location].discard(user)

    def process_negative_test(self, time, user):
        """
        Process a negative test event at the given time.
        If the user is infected, update their recovery time to be the earlier of the current recovery time or the test time.
        """
        if user in self.infection_info:
            inf_time, cont_time, rec_time = self.infection_info[user]
            if time < rec_time:
                self.infection_info[user] = (inf_time, cont_time, time)
                print(f"User {user} got a negative test at time {time}. Recovery time updated to {time}.")
    
    def get_total_infected(self):
        """
        Returns the total number of users that were ever infected.
        """
        return len(self.infection_info)


"""
Here it is possible that we learn something new every iteration thus O(n^3) where
n is the number of users. You can ask the candidate to try to build such a test case that would cause the
solution to be very slow.
"""

from collections import defaultdict
import time

class CovidSimulator:
    def __init__(self, K=0, X=float('inf')):
        """
        K: Incubation period (time units before a newly infected user becomes contagious)
        X: Recovery period (time units after infection at which a user recovers)
           (float('inf') means no recovery unless a negative test occurs)
        """
        self.K = K
        self.X = X
        # Maps location_id -> set of users currently present
        self.location_state = defaultdict(set)
        # Maps user_id -> (infection_time, contagious_time, recovery_time)
        self.infection_info = {}
    
    def process_arrival(self, time_stamp, user, location):
        # Check if any user already in the location is infectious
        exposed = False
        for other in self.location_state[location]:
            if other in self.infection_info:
                inf_time, cont_time, rec_time = self.infection_info[other]
                if cont_time <= time_stamp < rec_time:
                    exposed = True
                    break
        
        # Also check if the arriving user is already infectious
        if not exposed and user in self.infection_info:
            _, cont_time, rec_time = self.infection_info[user]
            if cont_time <= time_stamp < rec_time:
                exposed = True

        # If exposed and not already infected, infect the user.
        if exposed and user not in self.infection_info:
            infected_time = time_stamp
            contagious_time = time_stamp + self.K
            recovery_time = time_stamp + self.X
            self.infection_info[user] = (infected_time, contagious_time, recovery_time)
            # Uncomment the following line to see debug info:
            # print(f"User {user} infected at time {time_stamp}. Contagious at {contagious_time}, recovers at {recovery_time}.")
        
        # Add the user to the location.
        self.location_state[location].add(user)
    
    def process_departure(self, time_stamp, user, location):
        self.location_state[location].discard(user)
    
    def process_negative_test(self, time_stamp, user):
        if user in self.infection_info:
            inf_time, cont_time, rec_time = self.infection_info[user]
            if time_stamp < rec_time:
                self.infection_info[user] = (inf_time, cont_time, time_stamp)
    
    def get_total_infected(self):
        return len(self.infection_info)

def generate_worst_case_events(n):
    """
    Generates a worst-case scenario:
      - User 0 is initially infected and stays in location 0 for the entire duration.
      - For users 1..n-1, we schedule O(n) arrival/departure pairs in location 0.
    Total events: roughly 2*(n-1)*n + 2 for user 0 = O(n^2)
    And because each arrival might scan up to O(n) users, the worst-case work is O(n^3).
    """
    events = []
    
    # User 0 is initially infected and stays from time 0 to T_end.
    T_end = n * n + 10  # make sure it covers all events
    events.append({"time": 0, "type": "arrival", "user": 0, "location": 0})
    events.append({"time": T_end, "type": "departure", "user": 0, "location": 0})
    
    # For each other user, schedule n arrival-departure pairs that all overlap with user 0.
    for user in range(1, n):
        for j in range(n):
            t = 1 + j + user * n  # carefully chosen times to enforce many overlapping events
            events.append({"time": t, "type": "arrival", "user": user, "location": 0})
            events.append({"time": t + 0.5, "type": "departure", "user": user, "location": 0})
    
    # Sort events by time, and process departures before arrivals if timestamps tie.
    events.sort(key=lambda e: (e["time"], 0 if e["type"] == "departure" else 1))
    return events

def run_worst_case(n):
    simulator = CovidSimulator(K=0, X=10**6)  # Use large X to avoid recovery interference
    # Assume user 0 is initially infected:
    simulator.infection_info[0] = (0, 0, 10**6)
    
    events = generate_worst_case_events(n)
    
    start_time = time.time()
    for event in events:
        if event["type"] == "arrival":
            simulator.process_arrival(event["time"], event["user"], event["location"])
        elif event["type"] == "departure":
            simulator.process_departure(event["time"], event["user"], event["location"])
        elif event["type"] == "negative_test":
            simulator.process_negative_test(event["time"], event["user"])
    elapsed = time.time() - start_time
    print(f"Processed {len(events)} events in {elapsed:.3f} seconds.")
    print("Total infected users:", simulator.get_total_infected())

# Example: Increase n to see performance degrade.
if __name__ == "__main__":
    n = 200  # Adjust n to increase the worst-case load (n users with O(n^2) events)
    run_worst_case(n)


def build_infection_graph(visits, initial_infected):
    """
    Build a graph where each node represents a visit.
    Each visit is a tuple: (node_index, user, location, start, end)
    Two types of edges are added:
      - Consecutive visits for the same user.
      - Overlapping visits at the same location.
    Returns:
      nodes: a list of nodes
      graph: a dict mapping node index to a list of outgoing edges
             Each edge is represented as a tuple (edge_type, target_node_index)
             where edge_type is either "user" (for consecutive visits) or "loc" (for same-location overlap).
    """
    nodes = []
    # Assign a unique index to each visit.
    for idx, (user, loc, s, e) in enumerate(visits):
        nodes.append( (idx, user, loc, s, e) )
    
    # Partition nodes by user and by location.
    user_nodes = defaultdict(list)
    loc_nodes = defaultdict(list)
    for node in nodes:
        idx, user, loc, s, e = node
        user_nodes[user].append(node)
        loc_nodes[loc].append(node)
    
    # Sort visits for each user by start time.
    for user in user_nodes:
        user_nodes[user].sort(key=lambda node: node[3])
    
    # Sort visits for each location by start time.
    for loc in loc_nodes:
        loc_nodes[loc].sort(key=lambda node: node[3])
    
    # Build the graph.
    graph = defaultdict(list)
    
    # (a) Consecutive visits for same user.
    for user, nlist in user_nodes.items():
        for i in range(len(nlist)-1):
            from_idx = nlist[i][0]
            to_idx   = nlist[i+1][0]
            # Edge type "user" means that if the earlier visit is infected,
            # the next visit is infected at the start of that visit.
            graph[from_idx].append(('user', to_idx))
    
    # (b) Overlapping visits in the same location.
    # For each location, for each visit, add edges to all visits that start before the current visit ends.
    for loc, nlist in loc_nodes.items():
        # nlist is sorted by start time.
        for i in range(len(nlist)):
            idx_i, user_i, loc_i, s_i, e_i = nlist[i]
            # For all subsequent visits that start before e_i, check overlap.
            j = i + 1
            while j < len(nlist) and nlist[j][3] < e_i:
                idx_j, user_j, loc_j, s_j, e_j = nlist[j]
                # There is an overlap if:
                #    overlap_start = max(s_i, s_j)
                # and we need overlap_start < min(e_i, e_j)
                overlap_start = max(s_i, s_j)
                if overlap_start < min(e_i, e_j):
                    # Edge type "loc" indicates potential infection transmission
                    # from visit i to visit j.
                    graph[idx_i].append(('loc', idx_j))
                j += 1

    return nodes, graph

def propagate_infection(nodes, graph, initial_infected):
    """
    Run a propagation algorithm to compute the earliest infection time for each visit.
    For a node (visit) with interval [s, e], if it becomes infected at time t (with s <= t < e),
    then:
      - For a same-user edge to a later visit (of the same user), the infection time becomes that visit's start time.
      - For a same-location (overlap) edge, if the donor is infected at time t, then the recipient can be infected at time:
            candidate = max(t, recipient.start)
        provided candidate < donor.end and candidate < recipient.end.
    Returns an array infection_time such that infection_time[i] is the earliest time visit i is infected.
    """
    N = len(nodes)
    # Initialize infection times to infinity.
    inf_time = [math.inf] * N
    
    # For nodes belonging to an initially infected user, we can set the infection time
    # to the start time of that visit.
    for node in nodes:
        idx, user, loc, s, e = node
        if user in initial_infected:
            inf_time[idx] = s
    
    # Use a priority queue to propagate infection in increasing order of infection time.
    pq = []
    for i in range(N):
        if inf_time[i] < math.inf:
            heapq.heappush(pq, (inf_time[i], i))
    
    while pq:
        t, i = heapq.heappop(pq)
        if t > inf_time[i]:
            continue  # Skip outdated entry.
        idx, user, loc, s, e = nodes[i]
        # Process all outgoing edges from node i.
        for edge_type, j in graph[i]:
            idx_j, user_j, loc_j, s_j, e_j = nodes[j]
            if edge_type == "user":
                # For same-user edge, infection passes at the start of the next visit.
                candidate = s_j
            elif edge_type == "loc":
                # For same-location edge, if node i is infected at time t,
                # then candidate infection time for j is max(t, s_j)
                candidate = max(t, s_j)
                # But we must ensure that the donor is still present (t < e) and the recipient is present (candidate < e_j)
                if candidate >= e or candidate >= e_j:
                    continue
            else:
                continue

            if candidate < inf_time[j]:
                inf_time[j] = candidate
                heapq.heappush(pq, (candidate, j))
    
    return inf_time

def infection_via_graph(visits, initial_infected):
    """
    Given an array of visits (each of the form [user, location, start, end])
    and a list of initially infected users, builds a propagation graph and
    computes which users ultimately become infected.
    Returns the set of infected users.
    """
    nodes, graph = build_infection_graph(visits, initial_infected)
    inf_time = propagate_infection(nodes, graph, initial_infected)
    
    # A user is infected if any of his/her visits gets a finite infection time.
    infected_users = set()
    for node in nodes:
        idx, user, loc, s, e = node
        if inf_time[idx] < math.inf:
            infected_users.add(user)
    return infected_users

# Example usage:
if __name__ == "__main__":
    visits = [
        [0, 0, 1, 3],
        [0, 1, 4, 5],
        [0, 2, 8, 9],
        [1, 1, 4, 6],
        [2, 2, 7, 9],
        [3, 2, 6, 8],
    ]
    initial_infected = [1]
    infected_users = infection_via_graph(visits, initial_infected)
    print("Total infected users:", len(infected_users))
    print("Infected users:", infected_users)

