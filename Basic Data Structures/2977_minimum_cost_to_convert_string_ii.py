from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def djikstra(node):
            minhpq = [(0, node)]         # min heap storing (cost, node)
            min_cost_map = dict()        # stores the {node: cost}

            while minhpq:
                cost, curr = heappop(minhpq)

                # pass
                if curr in min_cost_map:
                    continue

                # mark as seen
                min_cost_map[curr] = cost

                # search for next candidates
                for neigh, neigh_cost in adj[curr]:
                    new_cost = cost + neigh_cost
                    heappush(minhpq, (new_cost, neigh))

            return min_cost_map

        def dfs(i):
            nonlocal n, lengths

            # base
            if i >= n:
                return 0

            # seen before
            if i in memo:
                return memo[i]

            # case1; 
            res = float('inf')

            # recur to index i + 1 if same value for ith index in source and target
            if source[i] == target[i]:
                res = dfs(i + 1)

            # recur on subset of source and target based on valid size length
            for size in lengths:
                # slice source and target string
                sub_s = source[i: i + size]
                sub_t = target[i: i + size]

                # run bfs for sub_s if substring sub_s 
                # does not exist in min_cost_maps
                if sub_s not in min_cost_maps:
                    min_cost_maps[sub_s] = djikstra(sub_s)    # append results to min_cost_maps

                # recur after sub_s if sub_t exist in min_cost_maps[sub_s]
                if sub_t in min_cost_maps[sub_s]:
                    cost = min_cost_maps[sub_s][sub_t]        # pull out cost from sub_s -> sub_t
                    new_i = i + size                          # new index after slicing
                    solution = cost + dfs(new_i)   

                    # compare  
                    res = min(res, solution)
                
            # allocate final res
            memo[i] = res

            return memo[i]

        # get the lenth of source strings
        lengths = set()

        # 1. build the directed graph
        adj = defaultdict(list)
        for src, des, c in zip(original, changed, cost):
            adj[src] += [(des, c)]
            lengths.add(len(src))

        # 2. stores min cost for each pair of (src, des)
        min_cost_maps = {ch: djikstra(ch) for ch in set(source)}

        n = len(source)

        # memo[i] := minimum cost to convert string/substring source to string/substring target starting at index i
        memo = dict()

        # 3. run dp starting at index 0 of source
        res = dfs(0)

        # 4. return -1 if dp result is inf
        return -1 if res == float('inf') else res