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
        h.append((matrix[row][0], row, 0))  # value, row, col. We've added the first element from every row in the range
    heapq.heapify(h)    
    while k:
        """
        Start extracting elements from the heap and add second, third, etc. element from a given row 
        """
        element, row, col = heapq.heappop(h)
        if col < len(matrix) - 1:
            heapq.heappush(h, (matrix[row][col + 1], row, col + 1))
        k -= 1
    return element 


def kthSmallest_binary_search(matrix, k):  # O(N*log(max - min)) and O(1)
    def countLessEqual(matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1
        return count, smaller, larger
    
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])
        count, smaller, larger = countLessEqual(matrix, mid, smaller, larger)
        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower
    return start


if __name__ == '__main__':
    print(kthSmallest_heap([[ 1,  5,  9], [10, 11, 13], [12, 13, 15]], 8))