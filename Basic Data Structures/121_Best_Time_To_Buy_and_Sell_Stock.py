import math
def maxProfit(prices):
    gl_max = 0
    if len(prices) < 2:
        return gl_max
    loc_min = prices[0]
    for k in prices[1:]:
        loc_min = min(k, loc_min)
        gl_max = max(gl_max, k-loc_min)
    return gl_max


def maxProfit_another(prices):
    if len(prices) < 2:
        return 0
    min_price = float('inf')
    profit = 0
    for p_ix in range(len(prices)):
        if prices[p_ix] < min_price:
            min_price = prices[p_ix]
        elif prices[p_ix] - min_price > profit:
            profit = prices[p_ix] - min_price
    return profit


def maxProfit_Kadane(prices):
    min_price = prices[0]
    glob_pr = -math.inf
    for p in prices[1:]:
        pot_profit = p - min_price
        min_price = min(min_price, p)
        glob_pr = max(glob_pr, pot_profit)
    return glob_pr if glob_pr > 0 else 0


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit_another([7, 1, 5, 3, 6, 4]))
    print(maxProfit_Kadane([7, 1, 5, 3, 6, 4]))