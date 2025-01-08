"""
Input to the function will be amount and portfolio object. return an object with the amount being equally distributed based on the portfolio given.


stocks: AAPL, EA, ATVI, OKTA, TEAM
portfolios: p1, ..., p4

* p1: 0.4 p2, 0.2 AAPL, 0.4 EA
 * p2: 0.4 p3, 0.4 p4, 0.2 AAPL
 * p3: 0.2 EA, 0.8 ATVI
 * p4: 0.6 OKTA, 0.4 TEAM```
 * 
Portfolio can be nested  : ```p1: 0.4 p2, 0.2 AAPL, 0.4 EA ```
Given the amount 1000$ and portfolio p4 as the input return as below
```/**
 * e.g. Input given is p4, $1000 -> {"OKTA": $600, "TEAM": $400, ......}
 * p1 ->  ??
 * p2 ->  ??
 * p3 -> ??
 */```
"""

def distribute_amount(amount, portfolio_name, portfolios):
    """
    O(N * M) -- portfolios and stocks
    O(N + S) -- recursion stack 
    Distributes the given amount across stocks based on portfolio definitions.
    :param amount: Total amount to distribute (float)
    :param portfolio_name: Name of the portfolio to distribute (str)
    :param portfolios: Dictionary defining portfolios and their allocations
    :return: Dictionary with stock names as keys and distributed amounts as values
    """
    result = {}

    def distribute(portfolio_name, amount):
        """Recursive helper function to process a portfolio."""
        portfolio = portfolios.get(portfolio_name)
        if portfolio is None:
            raise ValueError(f"Portfolio {portfolio_name} not found.")
        for key, weight in portfolio.items():
            allocation = amount * weight
            if key in portfolios:
                # Key is a nested portfolio, recurse
                distribute(key, allocation)
            else:
                # Key is a stock, add to result
                if key in result:
                    result[key] += allocation
                else:
                    result[key] = allocation

    distribute(portfolio_name, amount)
    return result

# Define portfolios
portfolios = {
    "p1": {"p2": 0.4, "AAPL": 0.2, "EA": 0.4},
    "p2": {"p3": 0.4, "p4": 0.4, "AAPL": 0.2},
    "p3": {"EA": 0.2, "ATVI": 0.8},
    "p4": {"OKTA": 0.6, "TEAM": 0.4}
}

# Example usage
amount = 1000
portfolio_name = "p4"
distribution = distribute_amount(amount, portfolio_name, portfolios)

print(distribution)

# Time Complexity:
# Let N be the total number of portfolios and stocks, and M be the maximum number of items in a portfolio.
# The function iterates over each portfolio and its items, recursively, so the complexity is O(N * M).
#
# Space Complexity:
# The space complexity is determined by the recursion depth, which in the worst case is O(N), and the size of the result dictionary, O(S), where S is the number of unique stocks.
# Overall space complexity: O(N + S).
