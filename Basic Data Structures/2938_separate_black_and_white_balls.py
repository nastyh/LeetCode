class Solution:
    def minimumSteps_stack(self, s: str) -> int:
        """
        O(n) both 
        see 1, add to the stack
        see 0, update by the value of the already seen ones
        """
        st, res = [], 0
        for ball in s:
            if ball == '1':
                st.append(ball)
            else:
                res += len(st)
        return res

    def minimumSteps_efficient(self, s: str) -> int:
        """
        O(n) and O(1)
        the more 1s we seen before 0s, the more our res grows. 
        Once we encounter 1, we increment white by 1 and keep track of what we've already seen
        """
        white, res, i = 0, 0, 0
        while i < len(s):
            if s[i] == '0':
                res += white
            white+= 1 if s[i] == '1' else 0
            i+= 1
        return res
    