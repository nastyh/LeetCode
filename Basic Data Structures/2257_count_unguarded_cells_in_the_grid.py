class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        res =  0
        matrix = [[0] * n for _ in range(m)]
        """
        O(mn) both
        build a matrix, fill out with what we have
        then process one by one and mark safe cells
        count them at the end
        """
        for r, c in guards:
            matrix[r][c] = 3 # mark guards
        for r, c in walls:
            matrix[r][c] = 2 # mark walls
        for val in guards:
            r, c = val[0], val[1]
            # look down
            for i in range(r + 1, m):
                if matrix[i][c] in (2, 3): 
                    break
                matrix[i][c] = 1 # mark as guarded
            #look up
            for i in range(r-1, -1, -1):
                if matrix[i][c] in (2,3):
                    break
                matrix[i][c] = 1 
            #look left
            for i in range(c + 1, n):
                if matrix[r][i] in (2, 3):
                    break
                matrix[r][i] = 1 
            # look right 
            for i in range(c - 1, -1, -1):
                if matrix[r][i] in (2, 3):
                    break
                matrix[r][i] = 1
        for i in range(m): # count for the answer
            for j in range(n):
                if matrix[i][j] == 0:
                    res+=1
        return res