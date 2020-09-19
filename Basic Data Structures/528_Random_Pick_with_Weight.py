import random
def __init__(self, w):
    self.w = w
	# 1. calculate relative frequency
    denom = sum(self.w)
    for i in range(len(self.w)):
        self.w[i] = self.w[i] / denom
    # 2. put relative frequencies on the number line between 0 and 1
	# Note self.w[-1] = 1
    for i in range(1,len(self.w)):
        self.w[i] += self.w[i-1]
    
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