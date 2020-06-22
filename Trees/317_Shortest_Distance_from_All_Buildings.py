 def shortestDistance(grid):
    ## RC ##
    ## APPROACH : BFS ##
    ## BRUTE FORCE: From each building, we do bfs and to every empty land and mark the distance in distances hashmap, after that we loop through all the empty lands and find the land which is least distant to all the buildings ##
    ## TIME COMPLEXITY : O(number of buildings * matrix) + O(marix * number of buildings) ~ O(2*N*N)
    
    if not grid : return 0
    n = len(grid)
    m = len(grid[0])
    builds = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                builds.append((i, j, 0))
    distances = collections.defaultdict(list)
    for build in builds:
        queue = [build]
        visited = set()
        while( queue ):
            i, j, d = queue.pop(0)
            for x, y in [ (0,1), (0,-1), (-1,0), (1,0) ]:
                if 0 <= i + x < n and 0 <= j + y < m and not (grid[ i+x ][ j+y ] >= 1 ) and (i+x, j+y) not in visited:
                    visited.add((i+x, j+y))
                    distances[(i+x,j+y)].append(d+1)
                    queue.append( (i+x, j+y, d+1) )
    ans = float('inf')
    for d in distances.values():
        if( len(d) == len(builds) ):
            ans = min( ans, sum(d) )
    return -1 if(ans == float('inf')) else ans
