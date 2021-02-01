def sortTransformedArray(nums, a, b, c):  # O(n) both
    """
    If a > 0, it's a parabola that decreases, increases
    if a < 0, it's a parabola that increases, decreases
    Two pointers, l and r. Compare values, if take a value, move the respective pointer after that
    """
    res = [0] * len(nums)
    ix = len(nums) - 1 if a > 0 else 0
    l, r = 0, len(nums) - 1

    def _helper(x, a, b, c):
        return a * x**2 + b * x + c

    while l <= r:
        l_val, r_val = _helper(nums[l], a, b, c), _helper(nums[r], a, b, c)
        if a > 0:
            if l_val > r_val:
                res[ix] = l_val
                l += 1
            else:
                res[ix] = r_val
                r -= 1
            ix -= 1
        else:
            if l_val < r_val:
                res[ix] = l_val
                l += 1
            else:
                res[ix] = r_val
                r -= 1
            ix += 1
    return res 


if __name__ == '__main__':
    print(sortTransformedArray([-4, -2, 2, 4], 1, 3, 5))
    print(sortTransformedArray([-4, -2, 2, 4], -1, 3, 5))