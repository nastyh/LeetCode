def brokenCalc(x, y):  # O(logY) and O(1)
    """
    Divide by 2 when y is even or add 1 to Y
    """
    if y <= x:
        return x - y
    else:
        res = 0
        while x < y:
            if y % 2 == 1:
                y += 1
            else:
                y = y // 2
            res += 1
        res += (x - y)
    return res