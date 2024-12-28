"""
A candidate has two sets of score - engagement and relevance score (es and rs respectively). Find how many candidates who's engagement and relevance score are greater than K other candidates.

i.e for candidate i --> there must be k candidates where es[i] > es[j] and rs[i] > rs[j]

e.g
es = [1, 2, 3, 4, 5]
rs = [1,2, 3, 4, 5]

K = 1
Output: 4 since all candidates except the 0th one have at least one other candidate where its engagement and relevance score is greater than another candidate
Implementation should be in O(n log n)
"""
def count_candidates(es, rs, K):
    """
    O(nlogn): sorting takes over
    O(n), n is the size of inputs es, rs
    """
    # Step 1: Pair engagement and relevance scores
    candidates = list(zip(es, rs))
    # Step 2: Sort candidates by engagement score
    # when processing a candidate, all prior candidates have es[j] < es[i]
    candidates.sort()
    # Step 3: Coordinate compression for relevance scores
    sorted_rs = sorted(set(rs))
    rank = {v: i + 1 for i, v in enumerate(sorted_rs)}  # 1-based indexing
    # Step 4: Initialize BIT (Fenwick Tree)
    n = len(sorted_rs)
    BIT = [0] * (n + 1)
    # For each candidate, query the BIT to find how many relevance scores are smaller than rs[i]
    def _update(index, delta):
        while index <= n:
            BIT[index] += delta
            index += index & -index
    def _query(index):
        total = 0
        while index > 0:
            total += BIT[index]
            index -= index & -index
        return total
    # Step 5: Process candidates and count valid ones
    valid_count = 0
    for _, r in candidates:
        # Query the number of relevance scores less than the current one
        count_less_than_r = _query(rank[r] - 1)
        if count_less_than_r >= K:
            valid_count += 1
        # Update the BIT with the current relevance score
        _update(rank[r], 1)
    return valid_count