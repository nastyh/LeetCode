def plusOne_short(digits):
    """
    Add 1 seperately
    Then process the rest starting from the second last digit in digits
    """
    res, carry = [], 0
    new_num = digits[-1] + 1
    res.append(new_num % 10)
    carry = new_num // 10
    for i in range(len(digits) - 2, -1, -1):
        new_num = carry + digits[i]
        res.append(new_num % 10)
        carry = new_num // 10
    if carry == 1:
        res.append(1)
    return res[::-1] 


def plusOne_optimal(digits):  # O(n) both
    """
    Solved in two steps
    1) add 1 to the last element. It can be either a single digit or a 10.
    If it's a 10, make carry equal to 1, otherwise there is no carry
    2) Then we will loop through the rest of the list.
    We start with the second last element in the list. We take a respective digit from digits and add carry.
    This number can be either a single-digit number or a 10. If it's a single-digit, just plant it to the respective index,
    if it is a 10, put zero and carry over 1.
    At the end of the day, if carry is not zero, insert 1 to the beginning (edge case such as [9, 9])
    """
    res = [None] * len(digits)
    carry = 0
    num = digits[-1] + 1
    if num == 10:
        res[-1] = 0
        carry = 1
    else:
        res[-1] = num
        carry = 0
    for i in range(len(digits) - 2, -1, - 1):
        curr = digits[i] + carry
        if curr == 10:
            res[i] = 0
            carry = 1
        else:
            res[i] = curr
            carry = 0
    if carry == 1:
        res.insert(0, 1)
    return res



def plusOne(digits):
    n = len(digits)
    # move along the input array starting from the end
    for i in range(n):
        idx = n - 1 - i
    # set all the nines at the end of array to zeros
        if digits[idx] == 9:
            digits[idx] = 0
    # here we have the rightmost not-nine
        else:
        # increase this rightmost not-nine by 1
            digits[idx] += 1
        # and the job is done
            return digits

    return [1] + digits

def plusOne_alt(digits):
    # return [x for x in str(int(''.join(map(str, digits))) + 1)]
    num = int(''.join([str(i) for i in digits])) + 1
    return [i for i in str(num)]

def plusOne_recursion(digits):
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        digits[-1] = 0
        digits[0:-1] = plusOne(digits[0:-1])
        return digits



if __name__ == '__main__':
    print(plusOne([1,9,9]))
    print(plusOne_alt([1,9,9]))
    print(plusOne_recursion([4]))
    print(plusOne_recursion([9]))
    print(plusOne_recursion([1, 9, 9]))


