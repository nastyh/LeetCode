import math
from typing import List


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """
        O(n) n times to calculate the distance for each point to the curr cand
        O(n) due to positions, nothing else?
        So that we don't get O(n^2) for every possible combination, 
        we can introduce weights inversely proportional to the Eucledian distance
        Weights ensure that points further away have less influence
        Starting point is the centroid (average of all candidates)
        Stopping: is when an update value < convergence threshold (epsilon)
        """
        if len(positions) == 1: return 0.0
        def calculate_total_distance(x, y):
            return sum(math.sqrt((x - px)**2 + (y - py)**2) for px, py in positions)

        x = sum(px for px, py in positions) / len(positions)
        y = sum(py for px, py in positions) / len(positions)

        epsilon = 1e-7  # Convergence threshold
        max_iterations = 1000

        for _ in range(max_iterations):
            numerator_x, numerator_y, denominator = 0.0, 0.0, 0.0
            for px, py in positions:
                distance = math.sqrt((x - px)**2 + (y - py)**2)
                # Avoid division by zero by skipping points very close to the current point
                if distance > epsilon:
                    weight = 1 / distance
                    numerator_x += weight * px
                    numerator_y += weight * py
                    denominator += weight

            if denominator == 0:
                break

            new_x = numerator_x / denominator
            new_y = numerator_y / denominator

            # Check for convergence
            if math.sqrt((new_x - x)**2 + (new_y - y)**2) < epsilon:
                break

            x, y = new_x, new_y

        return calculate_total_distance(x, y)