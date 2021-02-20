"""
https://codeforces.com/problemset/problem/160/A
"""
def twins(coins):  # O(nlogn) and O(1)
    res = 0
    left_sum, right_sum = 0, sum(coins)
    coins.sort(reverse = True)
    for coin in coins:
        left_sum += coin
        right_sum -= coin
        res += 1
        if left_sum > right_sum:
            return res


if __name__ == '__main__':
    print(twins([3, 3]))
    print(twins([2, 1, 2]))