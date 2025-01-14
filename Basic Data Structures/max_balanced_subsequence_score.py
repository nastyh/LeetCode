"""
Given a stock's prices for the past n days in the array stockPrice.
Choose a subsequence (an ordered subset of an array's elements) of stock prices, called chosenDays, 
such that the chosen subsequence of stock prices is balanced. The score of the chosen subsequence is the sum of
stock prices on the chosen days. Find the maximum possible score that can be obtained by choosing an optimally balanced subsequence.
The subsequence of stock prices is balanced if the following condition holds,
stockPrice[chosenDays[i]]-stockPrice[chosenDays[i-1]] = chosenDays[i]-chosenDays[i - 1], for i > 0.
"""
def MaxBalancedSubsequenceScore(n, stockPrice):
    """
    O(n) both 
    Store the difference between the stock price and the index for each element in diff.
    Store cumulative stock prices for each unique difference between stock prices and their positions.
    update the dict find the maximum cumulative stock price among all the balanced subsequences.
    Update the maxm variable if it finds a higher cumulative stock price.
    return maxm
    """
    # Create a dictionary to store
    # the difference and cumulative stock prices
    mp = {}
    maxm = 0
    for i in range(n):
        # Calculate the difference
        #  between stock price and index
        diff = stockPrice[i] - i

        # Add the stock price to
        #  the corresponding difference
        if diff in mp:
            mp[diff] += stockPrice[i]
        else:
            mp[diff] = stockPrice[i]

    # Find the maximum score
    #  by iterating through the dictionary
    for key, value in mp.items():
        if value > maxm:
            # Update the maximum score
            #  if a higher score is found
            maxm = value

    # Return the maximum score
    return maxm

def maxBalancedSubsequenceScore_dp(stockPrice):
    """
    O(n) both 
    """
    n = len(stockPrice)
    dp = [0] * n
    best_sum = {}
    
    for i in range(n):
        diff = stockPrice[i] - i
        if diff in best_sum:
            dp[i] = best_sum[diff] + stockPrice[i]
        else:
            dp[i] = stockPrice[i]
        
        best_sum[diff] = max(best_sum.get(diff, 0), dp[i])
    
    return max(dp)