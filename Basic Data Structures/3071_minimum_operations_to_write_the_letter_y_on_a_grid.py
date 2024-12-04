class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        """
        O(mn)
        O(1)
        Find the coordinates of the tops of the Y letter
        Indices to the idx list
        Put the elements beloging and not belonging to Y into separate lists
        two dictionaries to count the frequencies of the elements from the two lists above
        go over both of them and make a decision what is better to change 
        """
        n = len(grid)
        center_ix = (n // 2, n // 2) # middle of the grid cell
        top_left_diagonal = [(i, i) for i in range(n // 2)] # the upper left cell
        top_right_diagonal = [(i, n - i - 1) for i in range(n // 2)] # the upper right cell
        bottom_vertical = [(i, center_ix[1]) for i in range(center_ix[0], n)] # the lower middle cell + to the right
        idx = list(set(top_left_diagonal + [center_ix] + top_right_diagonal + bottom_vertical[1:])) # all these coordinates together

        y_elements = []
        non_y_elements = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in idx:
                    y_elements.append(grid[i][j])
                else:
                    non_y_elements.append(grid[i][j])

        operations = 0
        d1, d2 = Counter(non_y_elements), Counter(y_elements)
        if len(d1) == 1 and len(d2) == 1 and d1.keys() == d2.keys():
            return len(y_elements)
        for i in d1:
            for j in d2:
                # print(i, j)
                if i != j:
                    temp = d1[i] + d2[j]
                    if temp > operations:
                        operations = temp
                
        return n**2 - operations