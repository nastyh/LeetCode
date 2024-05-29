class BrowserHistory:
    """
    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, 
    you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history.
    If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

    """

    def __init__(self, homepage: str):
        """
        We need to store the history of the visited URLs, the best data structure to record the history is a stack data structure.
        The stack can store the elements (URLs) in the order they were given, with the most recently given element (URL) at the top 
        of the stack (i.e. last in first out order). The "back" operation can be implemented by popping the top element of the stack.   
        Now, to implement the "forward" operation, we can again use another stack.
        If we go "back" then we push the current URL into the "future" stack because when we do "forward"
        operations we would again want the most recently visited URL stored from the "future" data structure (i.e. in last in first out order).
        So, in this approach, we will use a string current to store the current URL, and two stacks history and future.
        Whenever we visit new URLs, we will push the current URL into the history stack which will be fetched while doing back operations,
        and whenever we do back operations, we store the URLs popped in the future stack which will be fetched while doing forward operations.
        """
        self._history, self._future = [], []
        # 'homepage' is the first visited URL.
        self._current = homepage
        

    def visit(self, url: str) -> None:
        # Push 'current' in 'history' stack and mark 'url' as 'current'.
        self._history.append(self._current)
        self._current = url
        # We need to delete all entries from 'future' stack.
        self._future = []
        

    def back(self, steps: int) -> str:
        # Pop elements from 'history' stack, and push elements in 'future' stack.
        while steps > 0 and self._history:
            self._future.append(self._current)
            self._current = self._history.pop()
            steps -= 1
        return self._current

    def forward(self, steps: int) -> str:
        # Pop elements from 'history' stack, and push elements in 'future' stack.
        while steps > 0 and self._future:
            self._history.append(self._current)
            self._current = self._future.pop()
            steps -= 1
        return self._current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)