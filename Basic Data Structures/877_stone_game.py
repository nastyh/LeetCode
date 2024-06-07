class Solution:
    def stoneGame(self, piles: List[int]) -> bool:  # O(n^2) both
        """
        two players can take left or right items
        Alice always starts
        True is she wins, False otherwise
        """
        # two dps that are lists of lists
        a = [[0] * len(piles) for _ in range(len(piles))]
        b = [[0] * len(piles) for _ in range(len(piles))]
        for j in range(len(piles)):
            a[j][j] = piles[j] # let's let Alice take the first one
            for i in range(j - 1, -1, -1): # from the other side
                # what she has + the neighbor or from the other side
                a[i][j] = max(piles[i] + b[i + 1][j], piles[j] + b[i][j - 1]) 
                # similarly for Bob but minimizing for him 
                b[i][j] = min(a[i + 1][j], a[i][j - 1])
        
        # her last result > than his 
        return a[len(piles) - 1][len(piles) - 1] > b[len(piles) - 1][len(piles) - 1]

    def stoneGame_another(self, piles: List[int]) -> bool:  # O(n^2) both
        """
        either we compare both players stones in the end to decide who wins,
        this way we need to keep two numbers, one for each player, or we can just
        record the max difference of stones between 'current' player and 'the other'
        player, if finally the difference is greater than 0, it means player 1 can win.
        """
        n = len(piles)
        f = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[j] = max(piles[i] - f[j], piles[j] - f[j - 1])
        return f[n - 1] > 0
        