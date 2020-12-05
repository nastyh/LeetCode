def canPlaceFlowers(flowerbed, n):
    flowers = 0
    p, f = 0, 0 # previous, following
    for i, c in enumerate(flowerbed):
            f = 0 if i + 1 >= len(flowerbed) else flowerbed[i+1]
            if p == c == f == 0:
                flowers += 1
                p = 1
            else:
                p = c
    return flowers >= n


def canPlaceFlowers_alt(flowerbed, n):
    """
    create a dp list with 0 at the ends to handle left and right elements
    Start iterating from the element at index 1 to the second last element and do greedily:
    if the previous, the current and the next are zeroes, put 1 into the current and decrement n.
    Check right here whether n == 0: if it is, immediately return True
    """
    if n == 0: return True
    dp = [0] + flowerbed + [0]
    for i in range(1, len(dp) - 1):
        if dp[i - 1] == 0 and dp[i] == 0 and dp[i + 1] == 0:
            dp[i] = 1
            n -= 1
            if n == 0: return True
    return False



def canPlaceFlowers_dp(flowerbed, n):  # doesn't pass the edge cases + uses extra space
    if n == 0: return True
    dp = [[i for i in flowerbed] for _ in range(len(flowerbed))]
    for row in range(1, len(flowerbed)):
        for col in range(len(flowerbed)):
            if col == 0:
                if n != 0:
                    if dp[row][col] == 0 and dp[row - 1][col + 1] == 0:
                        dp[row][col] = 1
                        n -= 1
                else:
                    return True
            elif col == len(flowerbed) - 1:
                if n != 0:
                    if dp[row][col] == 0 and dp[row - 1][col - 1] == 0:
                        dp[row][col] = 1
                        n -= 1
                else: return True
            else:
                if n != 0:
                    if dp[row][col] == 0 and dp[row - 1][col - 1] == 0 and dp[row - 1][col + 1] == 0 and dp[row][col - 1] == 0:
                        dp[row][col] = 1
                        n -= 1
                else:
                    return True
        return False


if __name__ == '__main__':
    # print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
    # print(canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(canPlaceFlowers_alt([1, 0, 0, 0, 1], 1))
    print(canPlaceFlowers_alt([1, 0, 0, 0, 1], 2))
    print(canPlaceFlowers_alt([1, 0, 0, 0, 0, 1], 2))
    print(canPlaceFlowers_alt([1, 0, 0, 0, 1, 0, 0], 2))




