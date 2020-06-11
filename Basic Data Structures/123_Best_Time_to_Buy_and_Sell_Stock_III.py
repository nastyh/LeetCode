def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1:
        return 0

    left_min = prices[0]
    right_max = prices[-1]

    length = len(prices)
    left_profits = [0] * length
    # pad the right DP array with an additional zero for convenience.
    right_profits = [0] * (length + 1)

    # construct the bidirectional DP array
    for l in range(1, length):
        left_profits[l] = max(left_profits[l-1], prices[l] - left_min)
        left_min = min(left_min, prices[l])

        r = length - 1 - l
        right_profits[r] = max(right_profits[r+1], right_max - prices[r])
        right_max = max(right_max, prices[r])

    max_profit = 0
    for i in range(0, length):
        max_profit = max(max_profit, left_profits[i] + right_profits[i+1])

    return max_profit


def maxProfit_alt(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        def helper(b, e, step): # helper function that finds maxrise and the locations of maxrise in prices[b:e:step]
            max_rise, tmp_lo, lo, hi = 0, b, 0, 0
            for i in range(b, e, step):
                rise = prices[i] - prices[tmp_lo]
                if rise <= 0:
                    tmp_lo = i
                elif rise > max_rise:
                    max_rise, lo, hi = rise, tmp_lo, i
            return max_rise, lo, hi

        # For the first pass, we identify the indices for "at most 1 transaction" problem, so that we find lo, hi
        max_rise, lo, hi = helper(0, l, 1)
        # Then there are three possibilities: 1, use (lo, hi) and another rise before lo; 2, (lo, hi) and another rise after hi; 3, use (lo, x) and (y, hi).
        # In the third case, it is equivalent to finding the max_rise in the sequence prices[hi:lo:-1]
        m1, m2, m3 = helper(0, lo, 1)[0], helper(hi+1, l, 1)[0], helper(hi-1, lo, -1)[0]
        return max_rise + max(m1, m2, m3)

if __name__ == '__main__':
    print(maxProfit([3,3,5,0,0,3,1,4]))
    print(maxProfit_alt([3,3,5,0,0,3,1,4]))
