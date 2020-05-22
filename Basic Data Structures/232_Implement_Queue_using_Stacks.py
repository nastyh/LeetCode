class MyQueue:

    def __init__(self):

        self.stack =[]
        self.stack1 =[]


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self.stack1 =self.stack[::-1]


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        i = self.stack1.pop()
        self.stack =self.stack1[::-1]
        return i


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if (len(self.stack)==0):
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
