from typing import List


class Solution:
    def numberOfAlternatingGroups_optimal(self, colors: List[int], k: int) -> int:
        """
        O(n) to go over
        O(n) to have a list alt to store adj tiles 
        Then we extend it to O(2n) but it's ok
        Sliding window is O(1)
        extra list alt where the value is 1 if the prev element 
        in colors is different 
        For a contiguous group starting at index i (of length k), the group is alternating if all consecutive pairs are alternating.
        Because the array is circular, when the window exceeds the end of alt, we can either use modulo arithmetic or double the alt array to handle wrap-around.
        When k is 1, no adjacent pair exists to compare, so every individual tile is a valid group, and the answer is simply n.
        """
        n = len(colors)
        # If k == 1, every tile is a valid alternating group.
        if k == 1:
            return n
        # Step 1: Precompute the alternation array.
        alt = [1 if colors[i] != colors[(i+1) % n] else 0 for i in range(n)]
        # Extend the alt array to handle circular wrap-around.
        alt_extended = alt + alt
        # Step 2: Use a sliding window of size (k-1) over the extended alt array.
        window_sum = sum(alt_extended[:k-1])
        count = 0
        # Check if the first window is valid.
        if window_sum == k - 1:
            count += 1
        # Slide the window from index 1 to n-1.
        for i in range(1, n):
            # Remove the element that is leaving the window and add the new element.
            window_sum += alt_extended[i+k-2] - alt_extended[i-1]
            if window_sum == k - 1:
                count += 1
        return count
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        Times out
        """
        res = 0
        for i in range(len(colors)):
            is_alt = True
            for j in range(1, k):
                if colors[(i + j - 1) % len(colors)] == colors[(i + j) % len(colors)]:
                    is_alt = False
                    break
            if is_alt:
                res += 1
        return res