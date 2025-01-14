from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        O(n^2) outer loop, inner loop for each num
        O(n) for sets
        """
        common_list = [0] * len(A)
        els_a, els_b = set(), set()
        for curr_ix in range(len(A)):
            els_a.add(A[curr_ix])
            els_b.add(B[curr_ix])
            common_count = 0 
            for el in els_a:
                if el in els_b:
                    common_count += 1
            common_list[curr_ix] = common_count
        return common_list
    
    def findThePrefixCommonArray_optimized(self, A: List[int], B: List[int]) -> List[int]:
        """
        O(n) both 

        """
        common_list = [0] * len(A) # will contain the counts of common prefixes 
        frequency = [0 for _ in range(len(A) + 1)] # keep track of the occurrences of each number
        common_count = 0
        for curr_ix in range(len(A)):
            """
            Increment frequency of current elements in A and B
            Check if the element in A has appeared before (common in prefix)
            """
            frequency[A[curr_ix]] += 1
            if frequency[A[curr_ix]] == 2:
                common_count += 1
            # same for B
            frequency[B[curr_ix]] += 1
            if frequency[B[curr_ix]] == 2:
                common_count += 1
            common_list[curr_ix] = common_count
        return common_list 
            
