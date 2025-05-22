from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        """
        O(cols^2 * rows) to try every pair of cols and iterate through each row
        O(rows) for the hashmap tracking prefix sumsper row-pair scan

        use a 2D prefix sum + hashmap approach, reducing it to a 1D subarray sum problem across all possible row pairs
        update each row to make it prefix sum: first col is the same, and to the right we add up values
        fix two rows r1 and r2, and for each column, compute the sum of elements between these two rows (inclusive)
        to create a 1D array of "column sums"
        the problem becomes: "How many subarrays of this 1D array sum to the target?"
        """
        rows, cols = len(matrix), len(matrix[0])
        res = 0

        # Precompute prefix sums for each row
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]

        # Now fix left and right columns and reduce the problem to 1D
        for c1 in range(cols):
            for c2 in range(c1, cols):
                counter = defaultdict(int)
                counter[0] = 1
                curr_sum = 0
                for r in range(rows):
                    # Sum between columns c1 and c2 for current row
                    row_sum = matrix[r][c2]
                    if c1 > 0:
                        row_sum -= matrix[r][c1 - 1]
                    curr_sum += row_sum
                    res += counter[curr_sum - target]
                    counter[curr_sum] += 1
        return res
