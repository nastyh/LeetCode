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


def maxProfit_fb_follow_up(prices):
    """
    return a list with min price and max price
    """
    res = [-1, -1]
    gl_profit = -math.inf
    if len(prices) < 2: 
        return res
    curr_pr = prices[0]
    for price in prices:
        pot_profit = price - curr_pr
        if pot_profit > gl_profit:
            gl_profit = pot_profit
            res[0] = curr_pr
            res[1] = price
        curr_pr = min(curr_pr, price)
    return res
    
def maxProfit_fb_follow_up_alt(array):
    if array == None or len(array) < 2:
        return None

    current_buy = array[0]
    global_sell = array[1]
    global_profit = global_sell - current_buy

    current_profit = -math.inf

    for i in range(1, len(array)):
        current_profit = array[i] - current_buy

        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = array[i]

        if current_buy > array[i]:
            current_buy = array[i];

    result = global_sell - global_profit, global_sell                 
    return result

if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit_another([7, 1, 5, 3, 6, 4]))
    print(maxProfit_Kadane([7, 1, 5, 3, 6, 4]))
    print(maxProfit_fb_follow_up([8, 5, 12, 9, 19, 1]))
    print(maxProfit_fb_follow_up([21, 12, 11, 9, 6, 3]))
    print(maxProfit_fb_follow_up_alt([21, 12, 11, 9, 6, 3]))