"""
You have a list of engagement ratings and relevant ratings for x pins

Eg [0.1. 0.4 0.2 0.5], [0.3, 0.1 0.1 0.6] find the number of pins whose engagement and relevant ratings
are strictly greater than K other pins where K is some integer that can change at runtime.

Eg: if K=2 then the answer is 1 as only the last pin is greater than atleast 2 other pins on both metrics.
"""

class FenwickTree:
    """
    data structure that supports 2 operations on a sequence of numbers
        Updating the value at a specific index (e.g., incrementing or setting).
        Querying the prefix sums (e.g., the sum of values from the start up to a given index).
    operations both run in O(logn)

    keep an auxiliary array (the Fenwick Tree array) of the same size (or size + 1 for 1-based indexing).
    Each position in the Fenwick Tree stores a partial sum of a range of elements in the original array.
    
    Uses the lowest set bit (LSB) of an index to decide the size of the range that index is responsible for.

    counts for each pin i, how many pins have both strictly lower engagement 
    and strictly lower relevance. 
    After computing this count for each pin, compare it to k and sum up
    how many meet the criteria

    """
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size + 1)  # 1-based indexing
    
    def update(self, idx, val):
        """Increments Fenwick Tree at position idx by val."""
        while idx <= self.size:
            self.data[idx] += val
            idx += idx & -idx # moves up the tree by jumping to the next responsible index
            # idx & -idx isolates the lowest set bit in the binary representation of i
            # ensures we visit each index that partially or fully covers ix position in the array
    
    def prefix_sum(self, idx):
        """Returns sum of values from 1 up to idx."""
        result = 0
        while idx > 0:
            result += self.data[idx]
            idx -= idx & -idx
        return result
    
    def range_sum(self, left, right):
        """Optional helper: sum over [left, right]."""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
    
def count_pins_exceeding_K_sorting_and_fenwick(engagement, relevance, K):
    """
    Time
    Compression: O(nlogn)
    Sorting: O(nlogn)
    Tree update/prefix sum is O(logn) done n times, hence, O(nlogn)
    Overall: O(nlogn)
    Space: O(n) for a Fenwick tree after compression

    After sorting by engagement ascending, every pin we process is guaranteed to have a larger or equal engagement than those already processed.
    Using a Fenwick Tree indexed by relevance, we maintain counts of pins
    that are smaller in engagement (since we processed them earlier)
    and we do a prefix sum query up to (compressed_relevance - 1) to ensure strict inequality.
    """
    n = len(engagement)
    # Step 1: Create list of (engagement, relevance, index)
    pins = [(engagement[i], relevance[i], i) for i in range(n)]
    
    # Step 2: Coordinate compress the relevance values
    # Extract all relevance values, sort and get unique
    unique_rels = sorted(set(r for (_, r, _) in pins))
    # Map each relevance to a compressed index from 1..len(unique_rels)
    rel_to_compressed = {val: idx+1 for idx, val in enumerate(unique_rels)}
    
    # Replace actual relevance with compressed
    for i in range(n):
        e, r, original_i = pins[i]
        pins[i] = (e, rel_to_compressed[r], original_i)
    
    # Step 3: Sort pins by engagement ascending; break ties by relevance ascending
    pins.sort(key=lambda x: (x[0], x[1]))
    
    # Step 4: Fenwick Tree to count how many pinned so far with smaller relevance
    fenwicks = FenwickTree(len(unique_rels))
    count_smaller = [0] * n  # count_smaller[i] = how many pins are smaller in both metrics than pin i
    
    # Process in ascending order of engagement
    for (eng_val, rel_val, orig_idx) in pins:
        # Number of pins with strictly lower relevance
        # We query fenwicks up to rel_val - 1
        count_smaller[orig_idx] = fenwicks.prefix_sum(rel_val - 1)
        
        # Insert this pin's relevance into Fenwick Tree
        fenwicks.update(rel_val, 1)
    
    # Step 5: Check how many pins exceed at least K others in both metrics
    answer = sum(1 for i in range(n) if count_smaller[i] >= K)
    return answer

def count_pins_exceeding_K_brute_force(engagement, relevance, K):
    """
    O(n^2) due to two loops
    O(1) don't store anything 
    """
    n = len(engagement)
    count_result = 0
    
    for i in range(n):
        # Count how many pins this pin i exceeds in both metrics
        exceed_count = 0
        for j in range(n):
            if i != j:
                if engagement[i] > engagement[j] and relevance[i] > relevance[j]:
                    exceed_count += 1
        
        # Check if pin i exceeds at least K pins
        if exceed_count >= K:
            count_result += 1
    
    return count_result