def palindrome_property():
    def is_palindrome_alt(n):
        new_n = ''
        t = n
        while t != 0:
            carry = t % 10
            new_n += str(carry)
            t = t // 10
        return int(new_n) == n

    def reverse_number(n):
        res = 0
        t = n
        for i in range(len(str(n)) - 1, -1, -1):
            carry = t % 10
            res += carry * 10**(i)
            t = t // 10
        return res

    res = []
    keep_going = True
    num = 10
    while keep_going:
        new_sum = num + reverse_number(num)
        if new_sum > 1000 and is_palindrome_alt(new_sum):
            res.append(num)
        if len(res) == 25:
            keep_going = False
        num += 1
    return res

if __name__ == '__main__':
    print(palindrome_property())
