import math

def maxProfit_optimal(prices):  # O(n) and O(1)
    """
    Cover an edge case
    Then we need to start somewhere. Let's say that the first number is the potential buy price.
    Then let's traverse the rest of the list.
    Every time we will calculate potential profit
    If this profit is positive, we need to make a transaction (kinda a greedy approach)
    After the transaction is done, we need to nullify our potential profit and update our current buying price
    Otherwise (if the potential profit is negative and we don't engage in a transaction),
    we need to decide if we want to hold to our current buying price or we rather take a smaller price (we prefer lower)
    """
    if len(prices) == 1: return 0
    res = 0
    curr_buy = prices[0]
    for i in range(1, len(prices)):
        pot_profit = prices[i] - curr_buy
        if pot_profit > 0:
            res += pot_profit
            curr_buy = prices[i]
            pot_profit = 0
        else:
            curr_buy = min(curr_buy, prices[i])
    return res



def maxProfit(prices):
    m_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            m_profit += prices[i] - prices[i - 1]
    return m_profit


def maxProfit_alt(prices):
    """
    First, find the long-term solution: this is Best Time to Buy and Sell Stock solved via Kadane's algorithm
    Second, find the short-term solution, or greedy: once you see an opportunity to make a profit, run a transaction. Keep the running sum of profits.
    There is a trick: if you make a transaction, you need to reassign st_min_price to the current price so that things don't overlap
    Third, return the max result between the two
    Finally, you can remove the long-term portion and just return st_running. It will still work. And it will be the solution above essentially. 
    """
    lt_min_price = prices[0]
    lt_glob_pr = -math.inf
    for p in prices[1:]:
        lt_pot_profit = p - lt_min_price
        lt_min_price = min(lt_min_price, p)
        lt_glob_pr = max(lt_glob_pr, lt_pot_profit)
    st_min_price = prices[0]
    st_running = 0
    for price in prices[1:]:
        if price > st_min_price:
            st_running += price - st_min_price
            st_min_price = price
        st_min_price = min(st_min_price, price)
    return max(st_running, lt_glob_pr)


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit_alt([7, 1, 5, 3, 6, 4]))
