from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        O(n!) permutations by exploring all possible ways to arrange a set of numbers
        Real time is faster due to early pruning in backtracking 
        O(n) due to the backtracking stack

         Try to place larger numbers first.
         To achieve this is to iterate from n down to 1 when deciding which number to put in an empty slot.
         For i ≥ 2 you try to place i at a position pos and then again at pos + i (provided both positions are free).
         For i = 1, since it only occurs once, you simply place it in one free slot.
        """
        res = [0] * (2*n - 1)
        used = [False] * (n + 1)
        def _helper(pos):
            if pos == 2*n - 1:
                return True
            # If current position is already filled, move on
            if res[pos] != 0:
                return _helper(pos + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    res[pos] = 1
                    used[1] = True 
                    if _helper(pos+1):
                        return True
                    res[pos] = 0
                    used[1] = False
                else:
                    # For numbers >=2, we need to check the position pos+num is in range and free.
                    if pos + num < 2*n-1 and res[pos] == 0 and res[pos + num] == 0:
                        res[pos] = num
                        res[pos + num] = num
                        used[num] = True
                        if _helper(pos + 1):
                            return True
                        # Backtrack: remove num from both positions
                        res[pos] = 0
                        res[pos + num] = 0
                        used[num] = False
            return False
        _helper(0)
        return res