from collections import deque
import math
def shortestSubarray(A, K): # doesn't work for edge cases
	if len(A) == 1:
		return 1 if A[0] == K else -1
	if A[0] >= K:
		return 1
	l, curr, min_l = 0, A[0], math.inf
	for i in range(1, len(A)):
		curr = max(curr + A[i], A[i])
		if A[i] >= curr + A[i]:
			l = i 
		if curr >= K:
			min_l = min(min_l, i - l + 1)
			# return i - l + 1
	return min_l if min_l != math.inf else -1

def shortestSubarray_alt(A, K): # alternative
        
        q = deque()
        q.append((-1,0))
        min_size = float("inf")
        
        cumsum = 0
        for j in range (len(A)):
            
            # scan from front of front/left of the queue
            cumsum = cumsum + A[j]
            while q and cumsum - q[0][1] >= K:                
                min_size = min(min_size, j - q[0][0])
                q.popleft() 
            
            # insert current cumsum while maintaing that cumsum should be greater elements in the back and q should in increasing order
            while q and q[-1][1] >= cumsum:
                q.pop()
            
            q.append((j,cumsum))
                
        return -1 if min_size == float("inf") else min_size

if __name__ == '__main__':
	# print(shortestSubarray([2,-1,2], 3))
	# print(shortestSubarray([1], 1))
	# print(shortestSubarray([1, 2], 4))
	# print(shortestSubarray([77,19,35,10,-14], 19))
	# print(shortestSubarray([17,85,93,-45,-21], 150))
	print(shortestSubarray_alt([2,-1,2], 3))
	print(shortestSubarray_alt([1], 1))
	print(shortestSubarray_alt([1, 2], 4))
	print(shortestSubarray_alt([77,19,35,10,-14], 19))
	print(shortestSubarray_alt([17,85,93,-45,-21], 150))

