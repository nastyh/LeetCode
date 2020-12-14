def cleanRoom(robot):  # O(N - M), N - num of cells, M - num of obstacles, O(N - M)
    """
    :type robot: Robot
    :rtype: None
    """
    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        
    def backtrack(cell = (0, 0), d = 0):
        visited.add(cell)
        robot.clean()
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        for i in range(4):
            new_d = (d + i) % 4  # to circle around
            new_cell = (cell[0] + directions[new_d][0], \
                        cell[1] + directions[new_d][1])
            
            if not new_cell in visited and robot.move():
                backtrack(new_cell, new_d)
                go_back()
            # turn the robot following chosen direction : clockwise
            robot.turnRight()

    # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    backtrack()


def cleanRoom_alt(robot):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cleaned = set()
    def dfs(robot, x, y, direction):
        if (x, y) in cleaned:
            return
        robot.clean()
        cleaned.add((x, y))
        for i, (dx, dy) in enumerate(directions[direction:] + directions[:direction]):
            nx = x + dx
            ny = y + dy
            if robot.move():
                dfs(robot, nx, ny, (direction + i) % 4)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
            else:    
                robot.turnRight()
    dfs(robot, 0, 0, 0) 