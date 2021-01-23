class MinStack:

    def __init__(self):
        self.s = []
        """
        initialize your data structure here.
        """


    def push(self, x: int) -> None:
        self.s.append(x)


    def pop(self) -> None:
        self.s.pop()


    def top(self) -> int:
        return self.s[-1] # returns the last element of the list (or stack in this case). Better than pop, b/c you can't pop from the empty stack

    def isEmpty(self): # it's a helper function. Without it, getMin() won't work for an empty stack
        return True if len(self.s) == 0 else False


    def getMin(self) -> int:
        return min(self.s) if not self.isEmpty() else -1



class MinStack:

     def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.currentMin = float('inf')
        self.prevMins = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.currentMin:
            self.prevMins.append(self.currentMin)
            self.currentMin = x

    def pop(self) -> None:
        if self.stack[-1] == self.currentMin:
            self.currentMin = self.prevMins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin