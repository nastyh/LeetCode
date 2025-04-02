from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        O(n) both
        work backwards and maintain a dp array where dp[i] represents the maximum points you can get starting from question i.
        for each question:
        If you skip it, you get dp[i+1] points.
        If you solve it, you earn the points from the current question and then jump
        to the next available question, which is at index i + brainpower[i] + 1.
        dp[i] = max(dp[i+1], points[i] + dp[i + brainpower[i] + 1]).
        """
        dp = [0] * (len(questions) + 1)
        for ix in range(len(questions) - 1, -1, -1):
            points, brainpower = questions[ix]
            next_ix = ix + brainpower + 1
            if next_ix < len(questions):
                solve = points + dp[next_ix]
            else:
                solve = points 
            skip = dp[ix + 1]
            dp[ix] = max(solve, skip)
        return dp[0]
    

    def mostPoints_from_left(self, questions: List[List[int]]) -> int:
        """
        same but from left to right
        skip: dp[i+1]=max(dp[i+1],dp[i])
        solve: dp[j]=max(dp[j],dp[i]+points[i]), j is i + brainpower[i] + 1
        """
        n = len(questions)
        dp = [0] * (n + 1)
    
        # Process each question from left to right.
        for i in range(n):
            points, brainpower = questions[i]
            
            # Option 1: Skip the question.
            dp[i + 1] = max(dp[i + 1], dp[i])
            
            # Option 2: Solve the question.
            next_index = i + brainpower + 1
            if next_index <= n:
                dp[next_index] = max(dp[next_index], dp[i] + points)
            else:
                dp[n] = max(dp[n], dp[i] + points)
        
        return dp[n]