import heapq, math
def minCostII_brute_force(costs):  # O(M*N*M) and O(1)
    if not costs: return 0
    M = len(costs)
    N = len(costs[0])
    for i in range(1, M):
        for j in range(N):
            costs[i][j] = costs[i][j] + min(costs[i - 1][:j] + costs[i - 1][j + 1:])
    return min(costs[-1])

 
def minCostII_optimized(costs):  # O(MN) and O(1) b/c it's just a heap of size 2
    """
    save 2 minimums from the prev row initially
    while going through j loop, you can directly use first minimum if the first minimum column and current column are not same.
    If the first minimum and current column are same THEN ONLY use second minimum
    """
    if not costs : return 0
    for i in range(1, len(costs)):
        mins = heapq.nsmallest(2, costs[i - 1])
        for j in range(len(costs[0])):
            costs[i][j] += mins[1] if costs[i - 1][j] == mins[0] else mins[0]
    return min(costs[-1])


def minCostII_another(costs):  # O(nk) and O(1)
    """
    store the minmum value and second minimum value from previous iteration/house
    current house has index i, the minimum cost for the house with paint color j
    is costs[i][j]+ Min(costs[i-1][k]). Here if k is the minimum cost color, but k==j,
    we have to use the second minimum cost color in previous iteration. So for each iteration,
    just keep two accumulated minimum costs for next iteration, until all houses have been painted. 
    """
    p_m1_cost, p_m1_idx, p_m2_cost, p_m2_idx = 0, -1, 0, -1
    for i in range(len(costs)):
        m1_cost, m1_idx, m2_cost, m2_idx = math.inf, -1, math.inf, -1
        for c_idx, c in enumerate(costs[i]):
            if c_idx != p_m1_idx:
                cost = c + p_m1_cost
            else:
                cost = c + p_m2_cost
            if cost < m1_cost:
                m1_cost, m1_idx, m2_cost, m2_idx = cost, c_idx, m1_cost, m1_idx
            elif cost < m2_cost:
                m2_cost, m2_idx = cost, c_idx
        p_m1_cost, p_m1_idx, p_m2_cost, p_m2_idx = m1_cost, m1_idx, m2_cost, m2_idx
    return p_m1_cost
