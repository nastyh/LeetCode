def productExceptSelf(nums):
    ll, rl = [None] * len(nums), [None] * len(nums)
    ll[0], rl[-1] = 1, 1

    for i in range(1, len(ll)):
        ll[i] = ll[i - 1] * nums[i - 1]

    for j in range(len(rl)-2, -1, -1):
        rl[j] = rl[j + 1] * nums[j + 1]

        """
        or instead of creating rl, we can update ll on the fly:
        right_prod = 1
        for j in range(len(ll) -1 , -1, -1):
            ll[j] = ll[j] * right_prod
            right_prod *= nums[j]

        return ll

        """

    return [x * y for (x, y) in zip(ll, rl)]
    """
    instead of zipping, we can generate the result as such (by default it returns a generator, so have to turn it into a list of lists and return the first element)
    res.append(list(ll[i] * rl[i] for i in range(len(nums))))
    return res[0]
    """

if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))
