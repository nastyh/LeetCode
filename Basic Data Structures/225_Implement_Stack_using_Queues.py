from collections import deque
class MyStack:  # most naive way
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque([])
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """ 
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """    
        return self.q.pop()


    def pop_alt(self):
        """
        Keep taking elements from the qeque, till one element is left. We will finally return it. But 
        before, we will put the rest of elements back 
        """
        l = len(self.q)
        for _ in range(l - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[-1]    

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0
