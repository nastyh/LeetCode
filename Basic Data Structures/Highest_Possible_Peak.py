'''

### Highest Possible Peak

Q: Given a 2D array "landscape" where True represents water and False represents land, generate a height map from the landscape and determine the height of the highest possible peak. The rules are: the height of any water cell is 0, the height of any land cell cannot differ by more than one from any
 of the neighboring (sharing one edge) cells. It is possible for two neighboring land cells to have the same height. Neighboring cells are only the horizontal and vertical neighbors.

You can assume that there is at least one water body in the landscape.

Input:
landscape = [ [True , False, False, False, False, False],
              [False, False, False, False, False, False],
              [False, False, False, False, False, False],
              [False, False, False, False, False, False],
              [False, False, False, False, False, True ] ]

Expected Output:
maxheight = 4

1. First pass through the grid
   - collect in the deque all water bodies in the form of [r, c, current_height]
2. Second pass grid
   - pop from the deque, process, append neighbors, increase height


T: O(MN), where M is the # of rows, N is the # of cols
S: O(MN), where M is the # of rows, N is the # of cols



'''

landscape_1 = [ [True , False, False, False, False, False],
              [False, False, False, False, False, False],
              [False, False, False, False, False, False],
              [False, False, False, False, False, False],
              [False, False, False, False, False, True ] ]

from collections import deque
import math
def highest_peak(landscape):
    def _helper_print(matrix):
        print(" ")
        for row in matrix:
            print(row)
        return 
    res = 0
#     def _helper(i, j, matrix):
#         current_height = 0
        
#         for y in range(len(matrix)):
#             for x in range(len(matrix[0])):
#                 if matrix[y][x] == True:
#                     q.append([y, x, 1])
        

        # q = deque([i, j, 0]) # first pass
        # while q: # second pass
        #     i_step, j_step, step = q.popleft()
        #     for r, c in (i_step + 1, j_step), (i_step - 1, j_step), (i_step, j_step - 1), (i_step, j_step + 1):
        #         if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
        #             if matrix[r][c] == True:
        #                 matrix[i_step, j_step] = step + 1
        #                 return
        #             q.append([r, c, step + 1])
    
    
    dp = [[-1] * len(landscape[0]) for _ in range(len(landscape))]  # not visited are -1
    q = deque()
    for y in range(len(landscape)):
        for x in range(len(landscape[0])):
            if landscape[y][x] == True:
                q.append([y, x, 0])
                dp[y][x] = 0
    while q:
        # _helper_print(dp)
        i_step, j_step, step = q.popleft()
        # print(i_step, j_step, step)
        for r, c in [(i_step + 1, j_step), (i_step - 1, j_step), (i_step, j_step - 1), (i_step, j_step + 1)]:
            if 0 <= r < len(landscape) and 0 <= c < len(landscape[0]) and dp[r][c] < 0:  # check we aren't out of bounds and haven't been to this cell
                if landscape[r][c] == False:
                    dp[r][c] = step + 1
                    res = max(res, step + 1)
                    q.append([r, c, step + 1])
    return res


if __name__ == '__main__':                                                 
    print(highest_peak(landscape_1))
                                                        
                                                        
                                                        
#                 dp[y][x] = 0
#             else:
#                 if y > 0:
#                     dp[y][x] = min(dp[y][x], dp[y - 1][x] + 1)
#                 if x > 0:
#                     dp[y][x] = min(dp[y][x], dp[y][x - 1] + 1)
                                                        
#     for y in reversed(range(len(landscape))):
#         for x in reversed(range(len(landscape[0]))):
                                                        
                 