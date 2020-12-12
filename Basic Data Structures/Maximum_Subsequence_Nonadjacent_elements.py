def find_max_sum_nonadjacent(a):
    """
    DP implementation: choose between a[i] + element two steps to the left, or just an element one step to the left
    """
    dp = [None] * len(a)
    dp[0], dp[1] = a[0], max(a[0], a[1])
    for i in range(2, len(a)):
        dp[i] = max(dp[i - 2] + a[i], dp[i - 1])
    return dp[-1]


def find_max_sum_nonadjacent_optimized(a):
    """
    Don't need to keep the whole array dp
    Need just two numbers: two steps to the left, and the max of two steps to the left and one step to the left
    """
    c, d = a[0], max(a[0], a[1])
    for i in range(2, len(a)):
        c, d = d, max(c + a[i], d)
    return d


if __name__ == '__main__':
    print(find_max_sum_nonadjacent([1, 6, 10, 14, -5, -1, 2, -1, 3]))
    print(find_max_sum_nonadjacent_optimized([1, 6, 10, 14, -5, -1, 2, -1, 3]))
    print(find_max_sum_nonadjacent([1, -1, 6, -4, 2, 2]))
    print(find_max_sum_nonadjacent_optimized([1, -1, 6, -4, 2, 2]))
