def minEatingSpeed(piles, H):

    def whether(piles, H, K):
        # print(K)
        total = [ (bananas+K-1)//K for bananas in piles]
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


if __name__ == '__main__':
    print(minEatingSpeed([30,11,23,4,20], 6))

