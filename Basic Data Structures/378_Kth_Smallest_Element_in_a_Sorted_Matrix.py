import heapq
def kthSmallest_brute_force(matrix, k):  # O(NM + klogn) --> O(NM) and O(NM) for a heap 
    """
    Got all value, drop in a heap, return the k-th smallest
    """
    nums = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            nums.append(matrix[row][col])
    return heapq.nsmallest(k, nums)[-1]


def kthSmallest_heap(matrix, k):  # min(K, len(matrix)) + K log(min(K, len(matrix))) and O(min(K, len(matrix))) for the heap
    """
    each row is a sorted list
    Take the first element of min(K, len(matrix)) and add each of these elems to the heap
    Also keep track of what row and col the elements are coming from.
    Once an element is popped, we have access to its row, col. We need to add the next right element, and it sits in row; col + 1
    """
    h = []
    for row in range(min(k, len(matrix))):
        # We add triplets of information for each cell
        h.append((matrix[row][0], row, 0))
    heapq.heapify(h)    
    while k:
        element, row, col = heapq.heappop(h)
        if col < len(matrix) - 1:
            heapq.heappush(h, (matrix[row][col + 1], row, col + 1))
        k -= 1
    return element  



[[ 1,  5,  9], [10, 11, 13], [12, 13, 15]]
if __name__ == '__main__':