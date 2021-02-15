import heapq
def kWeakestRows(mat, k):  # O(m * (n + logm)) mlogm for sorting and mn for summing; O(m) where n is rows and m is columns
    rows, ones, res = [], [], []
    for row in range(len(mat)):
        rows.append(row)
        ones.append(sum(mat[row]))
    # print(rows, ones)
    combined = zip(rows, ones)
    combined_sorted = sorted(combined, key = lambda x: (x[1], x[0]))
    return [strength for strength, _  in combined_sorted[:k]]
    # or we can build res manually
    # for ix in range(k):
    #     res.append(combined_sorted[ix][0])
    # return res


def kWeakestRows_with_bin_search(mat, k):  # O(m log(mn)) and O(m)
    """
    Slight improvement: find the first index of zero. It means that everything to the left is one
    This index is the sum of ones in this row.
    """
    rows, ones = [], []
    def _helper(nums):
        low = 0
        high = len(mat[0])
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] == 1:
                low = mid + 1
            else:
                high = mid
        return low
    
    for row in range(len(mat)):
        rows.append(row)
        ones.append(_helper(mat[row]))
    combined = zip(rows, ones)
    combined_sorted = sorted(combined, key = lambda x: (x[1], x[0]))
    return [strength for strength, _  in combined_sorted[:k]]


def kWeakestRows_vertical(mat, k):  # O(mn) and O(1)
    m = len(mat)
    n = len(mat[0])
    indexes = []
    # For each cell, accessed in the order shown in the animation.
    for c, r in itertools.product(range(n), range(m)):
        if len(indexes) == k: break
        # If this is the first 0 in the current row.
        if mat[r][c] == 0 and (c == 0 or mat[r][c - 1] == 1):
            indexes.append(r)

    # If there aren't enough, it's because some of the first k weakest rows
    # are entirely 1's. We need to include the ones with the lowest indexes
    # until we have at least k.
    i = 0
    while len(indexes) < k:
        # If index i in the last column is 1, this was a full row and therefore
        # couldn't have been included in the output yet.
        if mat[i][-1] == 1:
            indexes.append(i)
        i += 1
    return indexes


def kWeakestRows_queue(mat, k):  # O(mlog(nk)) and O(k) b/c of the queue
    m = len(mat)
    n = len(mat[0])
    def binary_search(row):
        low = 0
        high = n
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] == 1:
                low = mid + 1
            else:
                high = mid
        return low
    # Calculate the strength of each row using binary search.
    # Put the strength/index pairs into a priority queue.
    pq = []
    for i, row in enumerate(mat):
        strength = binary_search(row)
        entry = (-strength, -i)
        if len(pq) < k or entry > pq[0]:
            heapq.heappush(pq, entry)
        if len(pq) > k:
            heapq.heappop(pq)
    # Pull out and return the indexes of the smallest k entries.
    # Don't forget to convert them back to positive numbers!
    indexes = []
    while pq:
        strength, i = heapq.heappop(pq)
        indexes.append(-i)
    # Reverse, as the indexes are around the wrong way.
    indexes = indexes[::-1]
    return indexes
    return False 


if __name__ == '__main__':      
    print(kWeakestRows([[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3))
    print(kWeakestRows([[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], 2))
    print(kWeakestRows_with_bin_search([[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3))
    print(kWeakestRows_with_bin_search([[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], 2))
