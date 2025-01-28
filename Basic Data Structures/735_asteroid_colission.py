from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        O(n) both 
        st approach
        stack to maintain the current state of the asteroids in space after handling collisions
        If it is moving right (positive), push it onto the stack.
        If it is moving left (negative), check the stack
        If the stack is empty or the top of the stack is also moving left (negative), push the asteroid onto the stack.
        Otherwise, compare the sizes of the current asteroid and the top of the stack (moving right):
        If the top asteroid is smaller, pop it from the stack and continue comparing.
        If the top asteroid is larger, the current asteroid explodes (skip it).
        If both are the same size, both explode (pop the top asteroid and skip the current one).
        stack will contain the final state of the asteroids.
        """
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # Compare the size of the top of the stack with the current asteroid
                if stack[-1] < -asteroid:  # Top asteroid is smaller
                    stack.pop()  # Pop the smaller asteroid
                    continue  # Continue to check for more collisions
                elif stack[-1] == -asteroid:  # Both are the same size
                    stack.pop()  # Both explode
                break  # Current asteroid explodes or no further collision
            else:
                stack.append(asteroid)  # No collision, add asteroid to stack
        return stack