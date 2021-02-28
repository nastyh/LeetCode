from collections import defaultdict 
class FreqStack:  # O(N) both 
    """
    Maintain two stacks: one for frequency, and one for elements of this frequency 
    Have a dictionary mapping frequencies to elements 
    """
    def __init__(self):
        self.d = defaultdict(int)
        self.fst = []

    def push(self, x: int) -> None:
        self.d[x] = self.d[x] + 1
        freq = self.d[x]
        if freq > len(self.fst): #add a new frequency if not already present
            self.fst.append([])
        self.fst[freq - 1].append(x) #add an element to it's previous frequency + 1

    def pop(self) -> int:
        if self.fst:
            res = self.fst[-1][-1]
            self.d[self.fst[-1][-1]] -= 1
            self.fst[-1].pop() #pop the last element with max frequency
            if not self.fst[-1]: #If a frequency becomes empty, pop it
                self.fst.pop()
            return res