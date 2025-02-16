class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        O(n)
        O(1)
        person that wins has more consecutive sequences than another one
        find a sequence of three
        check whether it's A or B, increment accordingly
        compare at the end and return the winner 
        """
        a, b = 0, 0
        if len(colors) <= 1:
             return False
        for ix in range(1, len(colors) - 1):
            if colors[ix-1] == colors[ix] == colors[ix+1]:
                if colors[ix] == 'A':
                    a += 1
                else:
                    b += 1
        return a - b >= 1