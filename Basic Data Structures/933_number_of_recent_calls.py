class RecentCounter:
    """
    Initializes the counter with zero recent requests.

    """

    def __init__(self):
        self.curr_window = deque()
        

    def ping(self, t: int) -> int:
        """
        O(1) both since it's max 3000 iterations only
        
        Adds a new request at time t, where t represents some time in milliseconds,
        and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
        Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
        use a container such as array or list to keep track of all the incoming ping calls.
        At each occasion of ping(t) call, first we append the call to the container, and then starting from the current call,
        we iterate backwards to count the calls that fall into the time range of [t-3000, t].
        we could remove the outdated calls on the go, which can avoid the overflow of the container and reduce the memory consumption to the least.
        container will function like a sliding window over the ever-growing sequence of ping calls.
        """
        self.curr_window.append(t) # append the current call
        # remove outdated values that are outside the window of interest
        while self.curr_window[0] < t - 3000:
            self.curr_window.popleft()
        return len(self.curr_window)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)