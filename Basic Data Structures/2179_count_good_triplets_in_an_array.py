from typing import List

class FenwickTree:
    """
    Binary indexed tree 
    """
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        # BIT index is 1-indexed.
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        # Return sum of values from 0 to index (inclusive)
        index += 1
        result = 0
        while index:
            result += self.tree[index]
            index -= index & -index
        return result

class Solution:
    """
    O(nlogn) due to the Fenwick tree
    O(n), two trees of size O(n+1), then a dictionary, too 
    count the number of increasing subsequences of length 3
    good triplet condition pos1(x) < pos1(y) < pos1(z) and pos2(x) < pos2(y) < pos2(z)
    can be satisfied by first mapping one array onto the order of the other.
    """
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        """
        every value v we store its index in nums2: pos[v] = index of v in nums2
        Then transform nums1 by replacing each value w/ its corresponding index in nums2
        transformed[i] = pos[nums1[i]]
        if we read transformed in order and transformed[i] < transformed[j] < transformed[k] (i<j<k), then
        a triplet of elements is a good triplet 
        """
        pos = [0] * n
        for i, v in enumerate(nums2):
            pos[v] = i
        transformed = [pos[x] for x in nums1]

        bit1 = FenwickTree(n) # to count individual elements (subsequences of length 1)
        bit2 = FenwickTree(n) # to count pairs (subsequences of length 2)
        
        count_triplets = 0

        for x in transformed:
        # count of valid pairs ending with a value less than x gives triplets ending at this element.
            count_triplets += bit2.query(x - 1)
            # count of elements smaller than x, which form valid pairs with x as second element.
            count_pairs = bit1.query(x - 1)
            bit2.update(x, count_pairs)
            # update the count for x in BIT1.
            bit1.update(x, 1)
        return count_triplets
                