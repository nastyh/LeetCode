def addBinary(a, b):
    def binToDec(n):  # n is a string
        return sum([2**k if v=='1' else 0 for k,v in enumerate(n[::-1])])
    def decToBin_alt(n):  # n is a string
        res = []
        n = int(n)
        if n == 0: return '0'
        while n != 0:
            res.append(n % 2)
            n = n // 2
        return ''.join(str(i) for i in res[::-1])
    
    def decToBin(n): # n is an integer
        if n == 0:
            return 0
        result = ''
        while n != 0:
            remainder = n % 2  # gives the exact remainder
            n = n // 2
            result = str(remainder) + result
        return result
    c_dec = binToDec(a) + binToDec(b)
    return decToBin_alt(c_dec)


if __name__ == '__main__':
    print(addBinary('11', '1'))
    print(addBinary('1010', '1011'))
