 def getSmallestString(n, k):  # O(n) both
    res = ["a"] * n
    k -= n
    cur = n-1
    while k > 0:
        res[cur] = chr(ord("a") + min(k, 25))
        cur -= 1
        k -= 25
    return "".join(res)

def getSmallestString_alt(n, k):  # O(n) both
    res = ""
    for i in range(n - 1, -1, -1):
        add = min(k - i, 26)
        res += chr(add + ord('a') - 1)
        k -= add
    return res[::-1]