import random
def __init__(self, w):
    self.w = w
	# 1. calculate relative frequency
    denom = sum(self.w)
    for i in range(len(self.w)):
        self.w[i] = self.w[i] / denom
    # 2. put relative frequencies on the number line between 0 and 1
	# Note self.w[-1] = 1
    for i in range(1, len(self.w)):
        self.w[i] += self.w[i - 1]
    
def pickIndex(self) -> int:
	# this is where we pick the index
    N = random.uniform(0,1)
    flag = 1
    index = -1
	# test each region of the numberline to see if N falls in it, if it 
	# does not then go to the next index and check if N falls in it
	# this is gaurenteed to break because of previous normalization
    while flag:
        index +=1       
        if N <= self.w[index]:
            flag = 0
    return index


class Solution:  # more straightforward
    def __init__(self, w: List[int]):
        s = sum(w)
        self.weight = [w[0] / s]
        for i in range(1, len(w)):            
            self.weight.append(self.weight[-1] + w[i] / s)

    def pickIndex(self) -> int:
        l, r, seed = 0, len(self.weight) - 1, random.random()
        while l < r:
            m = (l+r) // 2
            if self.weight[m] <= seed: l = m + 1
            else: r = m
        return l


class Solution:
    """
    Have a list with cumulative sums and the total sum (self.s)
    Initialize a random number between 1 and self.s
    Look for this number in the list with cumulative sum.
    Return the index of the first occurance of this number by using binary search. If it doesn't exist, return the left number from where it would be
    """
    def __init__(self, w):  # O(N) both 
        self.w = w
        self.s = 0
        self.cum_sum = []
        for num in self.w:
            self.s += num
            self.cum_sum.append(self.s)
    
    def _bin_search(self, val):  # O(logN)
        l, r = 0, len(self.cum_sum) - 1
        while l < r:
            m = l + (r - l) // 2
            if self.cum_sum[m] < val:
                l = m + 1
            else:
                r = m
        return l

    def pickIndex(self):
        ix = random.randint(1, self.s)
        return self._bin_search(ix)