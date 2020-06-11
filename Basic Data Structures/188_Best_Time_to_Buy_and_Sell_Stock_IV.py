def maxProfit(prices, k):
    if(k == 0):
        return 0
    if(len(prices) == 0):
        return 0
    if(k > len(prices) / 2):
        #if k is large, we can take every possible transaction
        #the calculation is then very simple: take next_price - price whenever it is positive.
        profit = 0
        prices.append(0)
        for price, next_price in zip(prices[0:-1],prices[1:]):
            profit += max(0, next_price - price)
        return profit

    costs = [float('inf')] * k
    profits = [0] * k


    #costs[i] is the cost to acquire a stock on the ith purchase, adjusted for the maximum profit
    #obtaining on the previous (i-1) transactions.
    #profits[i] is the maximal profit obtained after the ith sale

    for p_ind, price in enumerate(prices):
        for i in range(min(k, (p_ind) // 2 + 1)):
            if(i == 0):
                costs[i] = min(costs[i], price)
            else:
                costs[i] = min(costs[i], price - profits[i-1])

            profits[i] = max(profits[i], price - costs[i])

    return max(profits)

if __name__ == '__main__':
    print(maxProfit([2,4,1], 2))
    print(maxProfit([3,2,6,5,0,3], 2))
