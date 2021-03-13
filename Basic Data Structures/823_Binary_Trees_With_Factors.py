import heapq
def numFactoredBinaryTrees(arr):
    # sort numbers so that we know that the factors of a number are to left. 
    arr.sort()
    # since all single digit tree's are valid, init dp solution with 1's
    T = [1] * len(arr)
    # As we calcuate, we need a look up for numbers after division with factors. 
    v = {}
    # Loop around to assume that you need to calcuate all trees with root a specific number. 
    for numidx in range(len(arr)):
        root_of_tree = arr[numidx]
        # Check all prev values to see which one's are potential factors
        for factor in range(0, numidx):
            # if the number is a factor then the divisor needs to also be in the prev numbers. 
            t = root_of_tree // arr[factor]
            if root_of_tree % arr[factor] == 0 and t in v:
                # if both factors exist, multiply to get full count of the tree
                T[numidx] += v[arr[factor]] * v[t]
        # Store the value of the root to for future lookups. 
        v[root_of_tree] = T[numidx]
    # Divide sum by mod to keep the ans in range. 
    return sum(T) % (10**9 + 7)


def numFactoredBinaryTrees_heap(A):  # O(N^2) and O(N)
    """
    if we find x*y = z in A, then cnt[z] += cnt[x]*cnt[y]. One caveat is that we have to process from small value to large value
    to make sure that when updating z the count of x and y are already accurate.
    use a priority queue to store (z, x, y) triplet, and process them one by one.
    """
    As = set(A) # set for O(1) lookup 
    pq = [] # min heap 
    for x, y in product(A, A): 
        if x*y in As:
            heapq.heappush(pq, (x*y, x, y))
    cnt = {x: 1 for x in A}
    while pq: 
        z, x, y = heapq.heappop(pq)
        cnt[z] += cnt[x] * cnt[y]
    return sum(cnt.values()) % 1_000_000_007