class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        """
        O(n^3) and O(1)
        the optimal placement in general is the median location between the houses
        they can be grouped together so the average won't really fly
        Put a mailbox so that it gives the median value of the distances between this
        mailbox and all the houses

        Base case is when k == 1, in which case we pick the mid house to be the position for the box.
        For cases k > 1, we simply parse the houses into 2 parts, solve the first parts with 1 and solve
        the rest with k-1; we keep the min result from such parsing.
        DFS can be used easily to achive this by specifying i (start location), j (end location), and k
        """
        houses.sort()
        n = len(houses)
        @cache
        def helper(i, j, k):
            # from house i to house j, k boxes
            if i == j: 
                return 0
            if k == 1: 
                l = j - i + 1
                mid = i + l // 2
                dist = 0
                for idx in range(i, j + 1):
                    dist += abs(houses[mid] - houses[idx])
                return dist
            else: 
                result = inf
                for idx in range(i, j):
                    result = min(result, helper(i, idx, 1) + helper(idx + 1, j, k - 1))
                return result

        return helper(0, n - 1, k)

    def minDistance_another(self, houses: List[int], k: int) -> int:
        """
        dp(i, j, k) means the total distance of houses[i:j+1] with k mailboxs at optimal locations.
        The base case is dp(i, j, 1). We compute mininum total distance by putting the only 1 mailbox
        at the median position of houses[i:j+1].
        Recurrence relationship: dp(i, j, k) = min( dp(i, m, k-1) + dp(m+1, j, 1) for m in range(i+k-2, j) ).
        For house[i: j+1] with k mailboxs, j >= i + k - 1 because two mailboxs cannot be put in one location.
        """
        houses.sort()
        @lru_cache(None)
        def dp(i, j, k):
            if k == 1: 
                total_distance = 0
                while i < j:
                    total_distance += houses[j] - houses[i]
                    i += 1
                    j -= 1
                return total_distance
            
            return min(dp(i,m,k-1) + dp(m+1,j,1) for m in range(i+k-2, j))
        
        return dp(0, len(houses)-1, k)