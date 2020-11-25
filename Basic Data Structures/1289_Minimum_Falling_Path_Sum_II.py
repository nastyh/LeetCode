from queue import PriorityQueue
from heapq import nsmallest
def minFallingPathSum(arr):
    dp = PriorityQueue()
    for i in range(len(arr[0])):
        dp.put((arr[0][i], i))
    
    
    for i in range(1, len(arr)):
        ndp = PriorityQueue()
        
        for j in range(len(arr[i])):
            
            takenOut = []
            while not dp.empty():
                elem = dp.get()
                val, ind = elem[0], elem[1]
                
                if ind!=j:
                    ndp.put((val+arr[i][j], j))
                    takenOut.append(elem)
                    break
                else:
                    takenOut.append(elem)
            
            for elem in takenOut:
                dp.put(elem)
        dp = ndp
    return dp.get()[0]


def minFallingPathSum_alt(arr):
    rows = len(arr)
    cols = rows
    if rows == 1:
        return arr[0][0]
    for row in range(1, rows):
        min_path_sum, min_path_sum_2nd = nsmallest(2, arr[row - 1])
        for col in range(cols):
            if arr[row - 1][col] == min_path_sum:
                arr[row][col] += min_path_sum_2nd
            else:
                arr[row][col] += min_path_sum
    return min(arr[rows - 1])  


if __name__ == '__main__':
    print(minFallingPathSum([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
    print(minFallingPathSum_alt([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))