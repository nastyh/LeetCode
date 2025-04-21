from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
        O(n) to process differences
        O(1) nothing to store 
        once you pick up the first element in a hidden sequence,
        the rest of the sequence is determined by the cum sums of differences 
        min_pref -- smallest offset possible relative to the starting element
        max_pref -- largest offset possible relative to the starting element
        """
        pref, min_pref, max_pref = 0, 0, 0
        for d in differences:
            pref += d
            min_pref = min(min_pref, pref)
            max_pref = max(max_pref, pref)
        # The first element h0 must lie in [lower - min_prefix, upper - max_prefix]
        low_h = lower - min_pref
        high_h = upper - max_pref
        # Count integer values in that interval
        return max(0, high_h - low_h + 1)