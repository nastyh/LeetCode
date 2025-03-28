from queue import PriorityQueue
from collections import deque
from typing import List


class Solution:
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    def maxPoints_heap(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        O(n*m*logn(nm) + k*log(nm))
        min-heap to perform a modified Dijkstra's traversal.
        In the worst case, all n⋅m cells are processed, and each heap operation (insertion or extraction)
        takes O(log(n⋅m)) time. Therefore, the time complexity for this part is O(n⋅mlog(n⋅m)).
        For each of the k queries, a binary search is performed on the thresholdForMaxPoints array,
        which has a size of (n⋅m)+1. Each binary search operation takes O(log(n⋅m)) time.
        Therefore, the time complexity for this part is O(klog(n⋅m)).
        O(nm)
        min heap mainly 
        """
        query_count = len(queries)
        result = [0] * query_count
        row_count = len(grid)
        col_count = len(grid[0])
        total_cells = row_count * col_count

        threshold_for_max_points = [0] * (total_cells + 1)
        min_value_to_reach = [
            [float("inf")] * col_count for _ in range(row_count)
        ]

        min_value_to_reach[0][0] = grid[0][0]

        # Min-heap for processing cells in increasing order of their maximum
        # encountered value.
        min_heap = PriorityQueue()
        min_heap.put((grid[0][0], 0, 0))
        visited_cells = 0

        # Dijkstra's algorithm to compute minValueToReach for each cell
        while not min_heap.empty():
            current = min_heap.get()

            # Store the value required to reach `visitedCells` points.
            threshold_for_max_points[visited_cells + 1] = current[0]
            visited_cells += 1

            # Explore all possible directions.
            for direction in self.DIRECTIONS:
                new_row, new_col = (
                    current[1] + direction[0],
                    current[2] + direction[1],
                )

                # Check if the new position is within bounds and not visited
                # before.
                if (
                    0 <= new_row < row_count
                    and 0 <= new_col < col_count
                    and min_value_to_reach[new_row][new_col] == float("inf")
                ):
                    # The max value encountered on the path to this cell.
                    min_value_to_reach[new_row][new_col] = max(
                        current[0], grid[new_row][new_col]
                    )

                    # Add the cell to the heap for further exploration.
                    min_heap.put(
                        (min_value_to_reach[new_row][new_col], new_row, new_col)
                    )

        # Use binary search to determine the maximum number of points that can
        # be collected for each query.
        for i in range(query_count):
            threshold = queries[i]
            left, right = 0, total_cells

            # Find the rightmost number of points we can collect before
            # exceeding the query threshold.
            while left < right:
                mid = left + (right - left + 1) // 2

                if threshold_for_max_points[mid] < threshold:
                    left = mid
                else:
                    right = mid - 1

            # Return `left`.
            result[i] = left

        return result

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        Brute force, TLE
        O(knm), k nun of queries, other two are sizes of grid
        O(mn) for visited
        """
        rows, cols = len(grid), len(grid[0])
        res = [0] * len(queries)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for q_ix, q_val in enumerate(queries):
            q = deque([(0, 0)])
            visited = [[0] * cols for _ in range(rows)]
            visited[0][0] = 1
            points = 0 
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    curr_row, curr_col = q.popleft()
                    print(f"curr_row is {curr_row} and curr_col is {curr_col}")
                    if grid[curr_row][curr_col] >= q_val:
                        continue
                    points += 1
                    for r_offset, c_offset in dirs:
                        new_r = curr_row + r_offset
                        new_c = curr_col + c_offset 
                        if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c] and grid[new_r][new_c] < q_val:
                            q.append((new_r, new_c))
                            visited[new_r][new_c] = 1 
                    res[q_ix] = points 
        return res 


# UNION FIND 
class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


class Query:
    def __init__(self, index, value):
        self.index = index
        self.value = value


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] < 0:
            return node
        return self.find(self.parent[node])

    def union(self, nodeA, nodeB):
        rootA = self.find(nodeA)
        rootB = self.find(nodeB)
        if rootA == rootB:
            return False

        if self.size[rootA] > self.size[rootB]:
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        else:
            self.parent[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        return True

    def get_size(self, node):
        return self.size[self.find(node)]


class Solution:
    ROW_DIRECTIONS = [0, 0, 1, -1]  # Right, Left, Down, Up
    COL_DIRECTIONS = [1, -1, 0, 0]  # Corresponding column moves

    def maxPoints(self, grid, queries):
        row_count, col_count = len(grid), len(grid[0])
        total_cells = row_count * col_count

        sorted_queries = [
            Query(i, val) for i, val in enumerate(queries)
        ]  # Store queries with their original indices to maintain result order
        sorted_queries.sort(
            key=lambda x: x.value
        )  # Sort queries in ascending order

        sorted_cells = [
            Cell(row, col, grid[row][col])
            for row in range(row_count)
            for col in range(col_count)
        ]  # Store all grid cells and sort them by value
        sorted_cells.sort(key=lambda x: x.value)  # Sort cells by value

        uf = UnionFind(total_cells)
        result = [0] * len(queries)

        cell_index = 0
        for query in sorted_queries:  # Process queries in sorted order
            while (
                cell_index < total_cells
                and sorted_cells[cell_index].value < query.value
            ):  # Process cells whose values are smaller than the current query value
                row = sorted_cells[cell_index].row
                col = sorted_cells[cell_index].col
                cell_id = (
                    row * col_count + col
                )  # Convert 2D position to 1D index

                for direction in range(
                    4
                ):  # Merge the current cell with its adjacent cells that have already been processed
                    new_row = row + Solution.ROW_DIRECTIONS[direction]
                    new_col = col + Solution.COL_DIRECTIONS[direction]
                    if (
                        0 <= new_row < row_count
                        and 0 <= new_col < col_count
                        and grid[new_row][new_col] < query.value
                    ):
                        uf.union(cell_id, new_row * col_count + new_col)

                cell_index += 1

            result[query.index] = (
                uf.get_size(0) if query.value > grid[0][0] else 0
            )  # Get the size of the component containing the top-left cell (0,0)

        return result
