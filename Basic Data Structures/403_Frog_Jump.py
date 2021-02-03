def canCross_dp_bottom_up(stones):  # O(N^2) both
    """
    Create dp of size stones. First is True b/c we're already there
    st_took is a list of set() for all positions, which notes down possible step length with which it can be reached from previous positions.
    At a particular position, check all the previous positions and calculate the steps required (st_need) from that position
    If a jump is possible , add the steps to the required position set() and mark it reachable inside dp
    """
    dp = [True] + [False] * (len(stones) - 1)
    steps_took = [set() for i in range(len(stones))]
    steps_took[0].add(0)    # base case
    for i in range(1, len(stones)):
        for j in range(i - 1, -1, -1):
            if dp[j]:
                st_need = stones[i] - stones[j]
                if(st_need - 1 in steps_took[j] or st_need in steps_took[j] or st_need + 1 in steps_took[j]):
                    steps_took[i].add(st_need)
                    dp[i] = True
    return dp[-1] 


def canCross_dp_top_down(stones):  # O(N^2) both
    def dfs(curr, prev, stones):
        if( (prev, stones[0]) in visited ): return False
        if( not(curr + prev == stones[0]) ): return False 
        if(len(stones) == 1): return True
        visited.add((prev, stones[0]))
        for next in [ prev + 1, prev, prev - 1 ]:
            for i in range(len(stones[1:])):
                # when the largest step itself cannot reach the first stone in the remaining, we break
                if( stones[0] + next < stones[i+1]): break
                if (dfs(stones[0], next, stones[i+1:])): return True
        return False
    visited = set()
    cache = {}
    return dfs(stones[0], 1, stones[1:])