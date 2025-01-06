class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        O(n) both
        two arrays to calculate the operations needed to bring all the balls from the left and right sides to the current box.
        Iterate through the string to calculate the cumulative operations for each box,
        first from left to right and then from right to left.
        Combine the results to calculate the total number of operations for each box.
        """
        n = len(boxes)
        answer = [0] * n
        # Pass from left to right
        balls = 0  # Count of balls to the left
        operations = 0  # Cumulative operations
        for i in range(n):
            answer[i] += operations
            balls += int(boxes[i])
            operations += balls
        # Pass from right to left
        balls = 0  # Count of balls to the right
        operations = 0  # Cumulative operations
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            balls += int(boxes[i])
            operations += balls
        return answer