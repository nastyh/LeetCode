from math import inf
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.currentMax = -math.inf
        self.prevMaxes = []
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x >= self.currentMax:
            self.prevMaxes.append(self.currentMax)
            self.currentMax = x
    
    def pop(self) -> None: # removes the max element in the stack
        if self.stack[-1] == self.currentMax:
            self.currentMax = self.prevMaxes.pop() # since the latest max is always in currentMax
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] # the max el in the stack

    def getMax(self) -> int:
        return self.currentMax
    
