class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        O(n) both to process and build the answer

        Add a virtual ‘L’ at the front and a virtual ‘R’ at the end, then process each interval between two non-‘.’ characters:
        We prepend an ‘L’ and append an ‘R’ so that every real domino lies between two “forces.”
        We keep two pointers, i and j, always pointing at non-‘.’ characters (i.e. a real ‘L’ or ‘R’)

        if s[i] == s[j], (both are L or both are R), everything between falls in the same way
        if s[i] == 'R' and s[j] =='L', they knock into each others 
        fill from both ends inward with ‘R’ on the left half and ‘L’ on the right half; a middle one (when the gap is odd) remains upright.

        if s[i] == 'L' and s[j] == 'R', no domino in between moves.
        """
        s = 'L' + dominoes + 'R'
        n = len(s)
        res = list(s)
        i = 0  # index of the last seen force
        for j in range(1, n):
            if s[j] == '.':
                continue
            # Now s[i] and s[j] are both in {'L','R'}, with only dots between.
            if s[i] == s[j]:
                # e.g. L....L or R....R => fill all between with same
                for k in range(i+1, j):
                    res[k] = s[i]
            elif s[i] == 'R' and s[j] == 'L':
                # e.g. R......L => fill inwards
                l, r = i+1, j-1
                while l < r:
                    res[l] = 'R'
                    res[r] = 'L'
                    l += 1; r -= 1
                # if l == r, it stays '.', as equal forces meet
            # else s[i]=='L' and s[j]=='R' => L....R, leave all '.' in between
            i = j

        # strip off the virtual ends
        return ''.join(res[1:-1])
