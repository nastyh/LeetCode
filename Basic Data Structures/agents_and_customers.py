"""
bank 
N agents
M customers before July
first come first serve
the customer will always choose the one with the lowest agent number. For agents, each of
them has a constant serving time that the ith agent will take times[i] minutes to serve a customer. 

Assume Julie arrived at time 0, and all the agents are idle and start to serve the customers.

We would like to know how many minutes Julie has to wait before meeting with an agent?

There are 3 agents with processing time 1min, 2min and 3min. 3 other people are currently
waiting in front of Julie. All 3 customers can be taken in by the 3 agents.
Given the first agent (index 0) will finish processing in 1min and then take in Julie, the waiting time here is 1 minute (return 1)
"""
import heapq

def agent_waiting_time(times, M):
    """
    O(MlogN). M is customers, N is the num of agents
    O(N) to store a heap of N agents
    Throw in a heap as a tuple of three elements 
    Take out M elements (a.k.a. people in line before you)
    the next element in the heap contains your answer 
    """
    
    h = [(0, i, times[i]) for i in range(len(times))]
    heapq.heapify(h)
    
    # Serve M customers before us
    for _ in range(M):
        next_available_time, agent_index, processing_time = heapq.heappop(h)
        heapq.heappush(h, (next_available_time + processing_time, agent_index, processing_time))
    # getting the next available agent
    res = heapq.heappop(h)[0]
    return res

# Example usage:
times = [1, 2, 3]
M = 3
print(agent_waiting_time(times, M))  # Output: 1

"""
Follow-up
M (number of customers) can become large
Thus, the loop will be running for a long time 
So we will have O(large number * log(small number))
Can we flip a solution so that we do O(small number * log(large number))
"""

def agent_waiting_time_binary_search(times, M):
    """
    O(NlogM)
    O(1) 
    directly compute when the M-th customer is served
    since we will be served next 
    Each agent processes customers at a constant rate, so we can binary search on time 
    Find the minimum time T such that M customers have been served.
    Count how many customers can be served by all N agents by time T.
    Adjust T accordingly.
    Once we have T, it's the time at which we will be served
    """
    def _helper(time):
        """
        how many customers have been served by time time 
        """
        return sum(time // t for t in times)
    l, r = 0, M * min(times) # r  here is the max time needed. All M customers being servied by the fastest agent 
    while l < r: 
        m = l + (r - l) // 2 
        if _helper(m) >= M: # how many customers are served by  m
            # if at least M are served, we go left, since we need the smallest time 
            r = m 
        else: # need more time to serve M customers, go right 
            l = m + 1 # increase time 
    # l is the min time when M customers are served
    return l 