class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def binToDec(n): # n is a string
            return sum([2**k if v=='1' else 0 for k,v in enumerate(n[::-1])])

        def decToBin(n): # n is an integer
            if n == 0:
                return 0
            result = ''
            while n != 0:
                remainder = n % 2  # gives the exact remainder
                n = n // 2
                result = str(remainder) + result
            return result


        a_dec = binToDec(a)
        b_dec = binToDec(b)

        return str(decToBin(a_dec+b_dec))

