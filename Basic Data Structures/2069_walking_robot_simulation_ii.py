class Robot:
    def __init__(self, width: int, height: int):
        """
        The constructor sets up the grid dimensions and computes the cycle length
        (the number of steps to complete one lap along the border). If the grid is
        degenerate (only one row or one column), the cycle length is adjusted accordingly.
        If it is a 1×1 grid, no movement is possible.
        """
        self.width = width
        self.height = height
        self.totalSteps = 0
        # Flag to check if any move has been executed.
        self.hasMoved = False
        
        # Special case: 1x1 grid never moves.
        if width == 1 and height == 1:
            self.cycle = 0
        # One-column grid: robot moves vertically.
        elif width == 1:
            self.cycle = 2 * (height - 1)
        # One-row grid: robot moves horizontally.
        elif height == 1:
            self.cycle = 2 * (width - 1)
        else:
            # Full grid: the robot always moves along the perimeter.
            self.cycle = 2 * (width + height - 2)

    def step(self, num: int) -> None:
        """
        The robot’s step counter is updated.
        (If the grid is 1×1, no steps are taken.) A flag (hasMoved) ensures that if no move is made, the initial direction "East" is returned.
        """
        # If grid is 1x1, no move is possible.
        if self.cycle == 0:
            return
        self.totalSteps += num
        self.hasMoved = True

    def getPos(self):
        """
        compute the effective step t along the cycle
        (using modulo arithmetic) and then determine the segment
        of the perimeter in which the robot is currently located. Based on that, they return the corresponding position and direction.
        """
        # If no move has been made, the robot is at the start.
        if self.cycle == 0 or self.totalSteps == 0:
            return [0, 0]
        # Compute effective steps along the cycle.
        t = self.totalSteps % self.cycle
        if t == 0:
            t = self.cycle

        # Case: full grid (width >= 2 and height >= 2)
        if self.width > 1 and self.height > 1:
            if t <= self.width - 1:
                return [t, 0]
            elif t <= (self.width - 1) + (self.height - 1):
                return [self.width - 1, t - (self.width - 1)]
            elif t <= (self.width - 1) * 2 + (self.height - 1):
                d = t - ((self.width - 1) + (self.height - 1))
                return [self.width - 1 - d, self.height - 1]
            else:
                d = t - (2 * (self.width - 1) + (self.height - 1))
                return [0, self.height - 1 - d]
        # Case: one-column grid.
        elif self.width == 1:
            if t <= self.height - 1:
                return [0, t]
            else:
                return [0, self.height - 1 - (t - (self.height - 1))]
        # Case: one-row grid.
        elif self.height == 1:
            if t <= self.width - 1:
                return [t, 0]
            else:
                return [self.width - 1 - (t - (self.width - 1)), 0]

    def getDir(self) -> str:
        # If no move has been made, direction remains "East".
        if self.cycle == 0 or self.totalSteps == 0:
            return "East"
        t = self.totalSteps % self.cycle
        if t == 0:
            t = self.cycle

        # Case: full grid.
        if self.width > 1 and self.height > 1:
            if t <= self.width - 1:
                return "East"
            elif t <= (self.width - 1) + (self.height - 1):
                return "North"
            elif t <= (self.width - 1) * 2 + (self.height - 1):
                return "West"
            else:
                return "South"
        # Case: one-column grid.
        elif self.width == 1:
            if t <= self.height - 1:
                return "North"
            else:
                return "South"
        # Case: one-row grid.
        elif self.height == 1:
            if t <= self.width - 1:
                return "East"
            else:
                return "West"
