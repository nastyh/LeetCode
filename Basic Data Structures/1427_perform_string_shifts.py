class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        """
        O(NL)  -- number of modifications and length of s respectively
        O(L)
        Do what is asked: accurately w/  the indices
        The % len(s) part is needed for cases when len(s) < number of steps in shift
        """
        res = [s]
        for command in shift:
            amount = command[1] % len(s)
            if command[0] == 0:
                current_result = res[-1][amount:] + res[-1][:amount]
                res.append(current_result)
            if command[0] == 1:
                current_result = res[-1][-amount:] + res[-1][:-amount]
                res.append(current_result)       
        return res[-1]