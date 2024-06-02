class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        """
        create a helper list dp, start filling it up from the end
        it stores the min cost of jumps to reach the end from the curr el
        cost of jumping from a curr el only depends on the numbers in front of us
        not behind the current element 
        we consider the possible positions (starting from the end of the list)
        so that the optimal one leads to a min cost of reaching the end 
        """
        res, dp, = [], [math.inf] * len(coins)
        dp[-1] = coins[-1]  # last is the same, it's where we need to arrive
        for i in range(len(coins) - 2, -1, -1):
            if coins[i] != - 1:  # just anywhere except -1
                for j in range(i + 1, min(len(coins), i + maxJump + 1)): # positioned at index 1 per the question
                    if dp[i] > dp[i] + coins[i]:
                        dp[i] = dp[j] + coins[i]
        if dp[0] == math.inf:
            return []
        curr_val = dp[0]
        for i in range(len(coins)):
            if dp[i] == curr_val:
                curr_val -= coins[i]
                res.append[i + 1]
        return res

    
        