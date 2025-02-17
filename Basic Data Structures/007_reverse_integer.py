def reverse_best(self, x: int) -> int:
        is_neg = 1
        new_x = x
        if x < 0: 
            is_neg = -1
            new_x = -x
        new_n = 0
        temp = new_x
        while temp > 0:
            new_n = new_n * 10 + temp % 10
            temp = temp // 10
        if new_n > 2**31 - 1: return 0
        return new_n * is_neg 


def reverse(x):
    if x > 0:  # handle positive numbers
        a =  int(str(x)[::-1])
    if x <=0:  # handle negative numbers
        a = -1 * int(str(x*-1)[::-1])
        # handle 32 bit overflow
    mina = -2**31
    maxa = 2**31 - 1
    if a not in range(mina, maxa):
        return 0
    else:
        return a



if __name__ == '__main__':
    print(reverse(123))
