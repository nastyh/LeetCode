from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        O(n*6^2*max(rollMax)), n is the num of rolls. rollMax[i] is the constraints
        O(n*6*max(rollMax))
        3d dp
        dp[i][j][k] num of valid sequences of length i where the seq ends
        with the face j+1 (1-indexed), and j+1 has been rolled consecutively
        k times
        For each i rolls, j (die face) and k (cons count)
        k > 1 --> dp[i[j][k] = dp[i-1][j][k-1] depends only on sequences ending with the same face
        k ==1 -->  can transition from all sequences of length i-1 that end with any other face:

        """
        MOD = 10**9 + 7
    
        # DP array
        dp = [[[0] * (max(rollMax) + 1) for _ in range(6)] for _ in range(n + 1)]
        
        # Base case
        for j in range(6):
            dp[1][j][1] = 1
        
        # Fill DP table
        for i in range(2, n + 1):
            for j in range(6):  # Current face
                for k in range(1, rollMax[j] + 1):
                    if k == 1:
                        # Transition from other faces
                        dp[i][j][k] = sum(dp[i-1][j2][k2] 
                                        for j2 in range(6) if j2 != j 
                                        for k2 in range(1, rollMax[j2] + 1)) % MOD
                    else:
                        # Transition from the same face with one less consecutive count
                        dp[i][j][k] = dp[i-1][j][k-1]
        
        # Calculate result
        result = sum(dp[n][j][k] for j in range(6) for k in range(1, rollMax[j] + 1)) % MOD
        return result