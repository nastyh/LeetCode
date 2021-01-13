def minEatingSpeed(piles, H):
    def whether(piles, H, K):
        # print(K)
        total = [ (bananas + K - 1) // K for bananas in piles]
        return sum(total) <= H
    left, right = 0, max(piles)
    while left < right: # O(lgn) for binary search, totally O(NlgN)
        mid = (left + right) / 2
            # print(left, right, mid)
        if whether(piles, H, mid): # this will take O(n)
            right = mid
        else:
            left = mid + 1
    return round(left)


def minEatingSpeed_alt(piles, H):  # O(nlogn) and O(1)
    """
    Binary search approach
    l = 1, r equals to the max number in piles
    m here is a number, not an index (like normally in a bin search)
    helper does the following: if chose 6 as a rate and pile is of the size of 13,
    how much time it'll take to eat the pile? It's 6 + 6 + 1, thus, it's 3 hours
    It returns whether we can improve the soluton
    """
    res = 0
    l, r = 1, max(piles)
    def _helper(piles, k, H):
        hours = 0
        for pile in piles:
            div = pile // k
            hours += div
            if pile % k != 0:
                hours += 1
        return hours <= H
    while l <= r:
        m = l + (r - l) // 2
        if _helper(piles, m, H):
            r = m - 1
        else:
            l = m + 1
    return l


if __name__ == '__main__':
    print(minEatingSpeed([30, 11, 23, 4, 20], 6))

