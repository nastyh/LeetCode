from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        O(F), F is the num of food items
        O(F + L), L is the snake's length
        """
        # screen size
        self.width = width
        self.height = height
        # list of food positions
        self.food = food
        # starting indices 
        self.food_index = 0
        self.snake = [(0, 0)]  # Snake starts at the top-left corner
        self.snake_set = {(0, 0)}  # Set for quick collision detection
        self.score = 0 # what to return

    def move(self, direction: str) -> int:
        """
        O(1) to update and to move
        Determine the new head position based on the direction (U, D, L, R).
        Check if the new head position goes out of bounds or collides with the snake's body
        If the new head position matches the current food item, the snake grows, and the score increases.
        If no food is consumed, the snake moves forward by removing the tail.
        """
        # Current head position
        head_x, head_y = self.snake[-1]

        # Calculate new head position based on the direction
        if direction == 'U':
            head_x -= 1
        elif direction == 'D':
            head_x += 1
        elif direction == 'L':
            head_y -= 1
        elif direction == 'R':
            head_y += 1

        # Check if the new head position is out of bounds
        if head_x < 0 or head_x >= self.height or head_y < 0 or head_y >= self.width:
            return -1
        # Check if the new head position collides with the snake's body
        new_head = (head_x, head_y)
        # Remove the tail from the set temporarily (it will move)
        tail = self.snake[0]
        if new_head in self.snake_set and new_head != tail:
            return -1
        # Check if the new head position is a food
        if self.food_index < len(self.food) and [head_x, head_y] == self.food[self.food_index]:
            self.food_index += 1
            self.score += 1
            # Do not remove the tail since the snake grows
        else:
            # Remove the tail (normal movement)
            self.snake_set.remove(tail)
            self.snake.pop(0)

        # Add the new head to the snake
        self.snake.append(new_head)
        self.snake_set.add(new_head)

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)