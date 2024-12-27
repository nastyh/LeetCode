"""
You are standing in line at a bank to open a bank account, there are M customers ahead of you and the bank has N agents
Each agent takes time[i] to serve a customer.
If multiple agents are available, a customer will always choose the agent with the lowest number
(i.e say agent 2,3,5 are available at some time, the next customer will choose agent 2)
Find out how many minutes it will take for you to be served by an agent
"""
import heapq
def time_to_be_served(M, N, times):
    """
    O((M+1)logN) both 
    M customers
    N agents 
    times per each agent to serve one person
    For each customer, the agent with the earliest availability is selected (i.e., the agent at the top of the heap).
    The agent’s availability is updated by adding the serving time for that agent
    After processing M + 1 customers (including you), available_time represents when you'll be served 
    """
    h = [(0, i) for i in range(N)] # (available times, indices of available agents)
    heapq.heapify(heap)
    # process the M customers in front of you
    for _ in range(M + 1):
        available_time, agent_index = heapq.heappop(h)
        heapq.heappush(h, (available_time + times[agent_index], agent_index))
    return available_time