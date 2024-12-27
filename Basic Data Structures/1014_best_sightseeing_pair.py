class Solution:
    def maxScoreSightseeingPair_brute_force(self, values: List[int]) -> int:
        """
        O(n^2) and O(1)
        just two loops, calculate everything, compare, pick the best
        Times out, though
        """
        glob_res, curr_res = -math.inf, -math.inf
        for l in range(len(values) - 1):
            for r in range(l+1, len(values)):
                curr_res = values[r] + values[l] + l - r
                glob_res = max(glob_res, curr_res)
        return glob_res

    def maxScoreSightseeingPair_Kadane(self, values: List[int]) -> int:
        """
        O(n) and O(1)
        It's a Kadane algorithm essentially
        values[i] + i is what the left part contributes
        values[j] - j is what the right part contributes
        Keep track of max values[i] + i seen so far
        use it to calculate the max score for values[j] - j as we iterate
        """
        res, max_left = -math.inf, values[0]
        for i in range(1, len(values)):
            res = max(res, max_left + values[i] - i) # potential max score for the pair (i;j)
            max_left = max(max_left, values[i] + i) # update to see the best left side score
        return res