class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        O(nlogn) and O(1)
        zip together sort from max to min based on the position
        time is eta: equal where you need to be minus where you are divided by time
        start putting eta in the stack
        if the time current time is worse than the previous one, add it
        Return the number of elements in the stack
        """
        stack = []
        for pos, speed in sorted(zip(position, speed), reverse = True):
            eta = (target - pos) / speed
            if not stack or eta > stack[-1]:
                stack.append(eta)
        return len(stack)

    def carFleet_dict(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        O(n) both
        """
        d = {}
        res = []
        for i in range(len(position)): 
            d[position[i]] = speed[i]
        position.sort()
        for p in position[::-1]: #traverse in reverse
            time = (target-p)/d[p] #track the current car's time to reach the goal
            if p == position[-1] or time > res[-1]: #if the current car requires more time than the last car, it turns into its own fleet
                res.append(time)

        return len(res)