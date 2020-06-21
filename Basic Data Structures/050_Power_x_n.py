def myPow(x, n):
    def _helper(n):
        ans = 1
        if(n == 0):
            return 1
        if(n==1):
            return x
        if(n == 2):
            return x * x

        if(n%2 == 0):
            ans = _helper(n//2)
            return ans * ans
        if( n%2 == 1):
            ans = _helper(n//2) * _helper((n//2) + 1)
            return ans

    if n < 0:
        x = 1 / x
        n = - n
    return _helper(n)

if __name__ == '__main__':
    print(myPow(2.0, 3))
    print(myPow(2.0, 0))
    print(myPow(2.0, -3))
