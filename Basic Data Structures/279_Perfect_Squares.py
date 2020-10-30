def numSquares_brute_force(n):
    """
    enumerate all possible combinations and find the minimal one of them.
    """
square_nums = [i**2 for i in range(1, int(math.sqrt(n))+1)]
def minNumSquares(k):
    """ recursive solution """
    # bottom cases: find a square number
    if k in square_nums:
        return 1
    min_num = float('inf')
    # Find the minimal value among all possible solutions
    for square in square_nums:
        if k < square:
            break
        new_num = minNumSquares(k-square) + 1
        min_num = min(min_num, new_num)
    return min_num
return minNumSquares(n)


def numSquares_dp(n):  # time O(n * sqrt(n)); space O(n)
    """
    As for almost all DP solutions, we first create an array dp of one or multiple dimensions to hold the values of intermediate sub-solutions, as well as 
    the final solution which is usually the last element in the array. Note that, we create a fictional element dp[0]=0 to simplify the logic, which helps in the case that the remainder (n-k) happens to be a square number.
    As an additional preparation step, we pre-calculate a list of square numbers (i.e. square_nums) that is less than the given number n.
    As the main step, we then loop from the number 1 to n, to calculate the solution for each number i (i.e. numSquares(i)). At each iteration,
     we keep the result of numSquares(i) in dp[i], while resuing the previous results stored in the array.
    At the end of the loop, we then return the last element in the array as the result of the solution.
    """
    square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]
    dp = [float('inf')] * (n+1)
    # bottom case
    dp[0] = 0
    for i in range(1, n+1):
        for square in square_nums:
            if i < square:
                break
            dp[i] = min(dp[i], dp[i-square] + 1)
    return dp[-1]


def numSquares_greedy(n):
     def is_divided_by(n, count):
        """
            return: true if "n" can be decomposed into "count" number of perfect square numbers.
            e.g. n=12, count=3:  true.
                    n=12, count=2:  false
        """
        if count == 1:
            return n in square_nums
        
        for k in square_nums:
            if is_divided_by(n - k, count - 1):
                return True
        return False
    square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    for count in range(1, n+1):
        if is_divided_by(n, count):
            return count