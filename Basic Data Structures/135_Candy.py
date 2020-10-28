def candy(ratings):  # doesn't work w/ edge cases 
    dp = [1] * len(ratings)
    dp[ratings.index(max(dp[0], dp[1]))] = dp[ratings.index(min(dp[0], dp[1]))] + 1
    for i in range(2, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            dp[i] = dp[i - 1] + 1
        elif ratings[i] == ratings[i - 1]:
            dp[i] = dp[i - 1]
    return sum(dp)


def candy_2_passes(ratings):
    dp = [1] * len(ratings)
    for i in range(len(ratings) - 1):
        if ratings[i + 1] > ratings[i]:
            dp[i + 1] = dp[i] + 1
    for j in range(len(ratings) - 1, 0, -1):
        if ratings[j - 1] > ratings[j]:
            dp[j - 1] = max(dp[j - 1], dp[j] + 1)
    return sum(dp)


if __name__ == '__main__':
    print(candy_2_passes([1, 0, 2]))