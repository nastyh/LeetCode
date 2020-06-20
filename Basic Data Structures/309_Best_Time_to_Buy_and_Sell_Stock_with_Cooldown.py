def maxProfit(prices):
    sold, held, reset = float('-inf'), float('-inf'), 0

    for price in prices:
        # Alternative: the calculation is done in parallel.
        # Therefore no need to keep temporary variables
        #sold, held, reset = held + price, max(held, reset-price), max(reset, sold)

        pre_sold = sold
        sold = held + price
        held = max(held, reset - price)
        reset = max(reset, pre_sold)

    return max(sold, reset)

def maxProfit_DP(prices):

        L = len(prices)
        # padding the array with additional zero to simply the logic
        MP = [0] * (L + 2)

        for i in range(L-1, -1, -1):
            C1 = 0
            # Case 1). buy and sell the stock
            for sell in range(i + 1, L):
                profit = (prices[sell] - prices[i]) + MP[sell + 2]
                C1 = max(profit, C1)

            # Case 2). do no transaction with the stock p[i]
            C2 = MP[i + 1]

            # sum up two cases
            MP[i] = max(C1, C2)

        return MP[0]
if __name__ == '__main__':
    print(maxProfit([1,2,3,0,2]))
    print(maxProfit_DP([1,2,3,0,2]))