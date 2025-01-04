"""
A candidate has two sets of score - engagement and relevance score (es and rs respectively).
Find how many candidates who's engagement and relevance score are greater than K other candidates.
i.e for candidate i --> there must be k candidates where es[i] > es[j] and rs[i] > rs[j]
e.g
es = [1, 2, 3, 4, 5]
rs = [1, 2, 3, 4, 5]
K = 1
Output: 4 since all candidates except the 0th one have at least one other candidate where its engagement and relevance score is greater than another candidate
Implementation should be in O(n log n)
"""
def count_candidates(es, rs, K):
    """
    Sorting O(nlogn)
    Coordinate compression O(nlogn) for sorting & ranking the unique relevance scores
    Fenwick tree operations: O(nlogn)
    Overall both are O(nlogn)

    FENWICK TREE EXPLAINED
    data structure that efficiently supports two operations on an array
    Prefix Sum Query: Get the sum of elements from the start of the array to a given index.
    Point Update: Update the value of an element in the array.
    done in O(logn)

    The Fenwick Tree is implemented as a flat 1D array.
    Each index in the tree stores a cumulative sum of a specific range of elements from the original array
    The range represented by each index in the tree is determined by the binary representation of the index.
    Specifically, it covers a power-of-2 range of elements.
    index i = 4 covers 4 elements [1, 2, 3, 4]
    index i = 6 covers 2 elements [5, 6]
    When you update a value in the array, the Fenwick Tree updates only the indices that depend on that value. This is done using the formula
    idx += idx & -idx
    To calculate the sum of elements from the start of the array to a given index,
    the Fenwick Tree aggregates sums from the relevant indices. This is done using
    idx -= idx & -idx
     isolates the rightmost set bit (the lowest bit that is 1) in the binary representation of idx.

    Combine Scores: Pair engagement scores (es) with relevance scores (rs) to form tuples
    Sort the candidates based on their engagement scores (es).
    This ensures that when we process relevance scores (rs), we only need to focus on candidates with smaller engagement scores.
    Use a Fenwick Tree (Binary Indexed Tree) to keep track of the number of relevance scores that have already been processed.
    For each candidate, count how many relevance scores are smaller than the current candidate's relevance score and compare it to K
    Count the number of candidates that satisfy the condition.
    """
    n = len(es)
    candidates = list(zip(es, rs))  # Pair es and rs
    candidates.sort()  # Sort by engagement score (es)
    # Coordinate compression for rs
    unique_rs = sorted(set(rs))
        rank = {val: idx + 1 for idx, val in enumerate(unique_rs)}  # Rank starts from 1
    BIT = [0] * (len(unique_rs) + 1)
    def _update(idx, val):
        """Update BIT at index idx by val."""
        while idx < len(BIT):
            BIT[idx] += val
            idx += idx & -idx
    def _query(idx):
        """Query the sum of BIT up to index idx."""
        total = 0
        while idx > 0:
            total += BIT[idx]
            idx -= idx & -idx
        return total
    
    count = 0
    for _, relevance in candidates:
        # Query BIT for counts of relevance scores less than current relevance
        rank_relevance = rank[relevance]
        num_less = _query(rank_relevance - 1)
        
        if num_less > K:
            count += 1
        
        _update(rank_relevance, 1)
    return count