class Leaderboard:

    def __init__(self): # space is O(N+K) where N for the dict, K for the heap
        # bruteforce is just to have a dict, resort it, 
        # keep track of the K elements
        # we will do w/ a heap
        self.d = {} # just mapping

    def addScore(self, playerId: int, score: int) -> None:  # O(1)
        # add to the dict
        if playerId not in self.d:
            self.d[playerId] = score
        else:
            self.d[playerId] += score
        

    def top(self, K: int) -> int: # O(K)+O(NlogK) = O(NlogK) 
        """
        Start using a min heap
        Iterate over the first K elements in the dictionary
        and throw into a heap
        We maintain exactly K elements all the times
        Do it for N - K elements 
        Then just add everything that is left
        This will be the k largest values (so we don't flip the sign)
        """
        h = []
        for v in self.d.values():
            heapq.heappush(h, v)
            if len(h) > K:
                heapq.heappop(h)
        res = 0
        while h:
            res += heapq.heappop(h)
        return res
        

    def reset(self, playerId: int) -> None: # O(1)
        self.d[playerId] = 0


    # and just w/ sorting and defaultdict
    # O(nlogn) due to sorting 

    def __init__(self):
        self.leaderboard = defaultdict(int)
    
    def addScore(self, playerId: int, score: int) -> None: 
        self.leaderboard[playerId] += score
        
 
    def top(self, K: int) -> int:
        return sum(sorted(self.leaderboard.values(), reverse = True) [:K])

    def reset(self, playerId: int) -> None:
        self.leaderboard.pop(playerId) # since it's sorted from above
        
    
    # with max heap
    def __init__(self):
        self.d = {}
        self.h = []


    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.d:
            self.d[playerId] = score
            heapq.heappush(self.h, (-score, playerId))
        else:
            h2 = []
            self.d[playerId] += score
            while self.h:
                x = heapq.heappop(self.h)
                if x[1] == playerId:
                    heapq.heappush(self.h, (-1 * score + x[0], playerId))
                    break
                else:
                    heapq.heappush(h2,x)
            while h2:
                heapq.heappush(self.h, heapq.heappop(h2))
      
      def top(self, K: int) -> int:
        x = heapq.nsmallest(K,self.h)
        sm = 0
        for i in x:
            sm += abs(i[0])
        return sm
    
    def reset(self, playerId: int) -> None:
        del self.d[playerId]
        heap2 = []
        while self.h:
            x = heapq.heappop(self.h)
            if x[1] == playerId:
                break
            else:
                heapq.heappush(heap2,x)
        while heap2:
            heapq.heappush(self.h, heapq.heappop(heap2))
        



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)