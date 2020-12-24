def minCost(s, cost):  # O(n) and O(1)
    ans = 0
    l, r = 0, 1
    while r < len(s):
        if s[l] != s[r]:
            l = r 
            r += 1
        else:
            ans += min(cost[l], cost[r])
            if cost[l] < cost[r]:
                l = r
                r += 1
            else:
                r += 1
    return ans


if __name__ == '__main__':
    print(minCost('abaac', [1, 2, 3, 4, 5]))
    print(minCost('abc', [1, 2, 3]))
    print(minCost('aabaa', [1, 2, 3, 4, 1]))
    print(minCost('aaabbbabbbb', [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]))
    print(minCost('cddcdcae', [4, 8, 8, 4, 4, 5, 4, 2]))