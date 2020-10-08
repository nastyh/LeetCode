def bitwiseComplement(N):
    if N == 0: return 1
    def dec2Bin(x): 
        res = ''
        while x != 0:
            rem = x % 2
            res += str(rem)
            x = x // 2 
        return res[::-1]
    
    def bin2Dec(y):
        return sum([2**k if v == '1' else 0 for k, v in enumerate(list(reversed(y)))])
    
    n_binary = dec2Bin(N)
    n_binary_reversed = ''.join([str(1) if n == '0' else str(0) for n in n_binary])
    return bin2Dec(n_binary_reversed)