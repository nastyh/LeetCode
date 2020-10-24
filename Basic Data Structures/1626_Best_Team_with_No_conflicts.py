def bestteamscore(scores, ages):  # O(n^2)
    """
    zip and sort both by age
    technically, after it we don't need ages anymore
    we know that the consecutive scores are associated with higher ages
    start making greedy decisions:
    for every element (r) we need to go over all previous elements (l)
    if the right score > than the left score, choose the max between dp[r] or taking dp[l] and adding to it potential player items[r][1]
    P.S. We can also sort by age but in the reversed order. Then, when comparing, we need to do items[r][1] <= items[l][1]
    """
    items = list(zip(ages, scores))
    items.sort()
    dp = [0] * len(items)
    res = 0
    for r in range(len(items)):
        dp[r] = items[r][1]
        for l in range(r):
            if items[r][1] >= items[l][1]:
                dp[r] = max(dp[r], items[r][1] + dp[l])
    return max(dp)


if __name__ == '__main__':
    print(bestteamscore([1 , 2,  3, 5], [8, 9, 10, 1]))
    print(bestteamscore([1 , 3,  5, 10, 15], [1, 2, 3, 4, 5]))
    print(bestteamscore([4, 5, 6, 5], [2, 1, 2, 1]))