def addStrings(num1, num2):
    # Grab the length of longest one
    max_length = max(len(num1), len(num2))
    result = []
    carry = 0
    for index in range (1, max_length + 1):
        # Walk from the end back
        rev_index = index * - 1
        # Place zero if other array is longer
        digit1 = num1[rev_index] if index < len(num1) + 1 else 0
        digit2 = num2[rev_index] if index < len(num2) + 1 else 0
        # Add the current number column
        s = str(int(digit2) + int(digit1) + carry)
        # Determine if we have a carry
        if len(s) == 2:
            carry = int(s[0])
            result.insert(0, s[1])
        else:
            carry = 0
            result.insert(0, s[0])
    # Special case of a carry on last addition
    if carry:
        result.insert(0, "1")
    return "".join(result)


def addStrings_ord(num1, num2):  # same as above and below but w/o using int and with or in the main loop
    res = []
    carry = 0
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    while p1 >= 0 or p2 >= 0:
        x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
        x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
        value = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10
        res.append(value)
        p1 -= 1
        p2 -= 1
    if carry:
        res.append(carry)
    return ''.join(str(x) for x in res[::-1])


def addStrings_alt(num1, num2):  # O(max(len(num1), len(num2))) both
    """
    Another approach.
    Add digits by digits until the shorter string ends
    Process the remaining portion taking carry of the carry
    Take care of the carry one more time at the end 
    """
    res = []
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    while i >= 0 and j >= 0:  # loop ends, index of the shorter string is at zero, index of the longer string on step to the left 
        num = int(num1[i]) + int(num2[j]) + carry
        res.append(num % 10)
        carry = num // 10
        i -= 1
        j -= 1
    while i >= 0:
        num = int(num1[i]) + carry
        carry = num // 10
        res.append(num % 10)
        i -= 1
    while j >= 0:
        num = int(num2[j]) + carry
        carry = num // 10
        res.append(num % 10)
        j -= 1
    if carry != 0:
        res.append(1)
    return ''.join(str(i) for i in res)[::-1]  # ''.join(res)[::-1] won't work 


def addStrings_power_tens(num1, num2):
    def _helper(num):
        l = num.split()
        total = 0
        for k, v in enumerate(l[::-1]):
            total += ((10**k) * int(v))
        return total
    return str(_helper(num1) + _helper(num2)) 


def addStrings_slow(num1, num2):
    t1 = sum([v * 10**k for k, v in enumerate([int(i) for i in num1][::-1])])
    t2 = sum([v * 10**k for k, v in enumerate([int(i) for i in num2][::-1])])
    return str(t1 + t2)


from itertools import zip_longest
def addStrings_zip_longest(num1, num2):
    # this part is called for every pair of digits in num1 and num2 by zip longest
    # a and b are both tuples, a represents (0,nums1[i]) and b represents (is_there_carryover? , nums2[i])
    # the output is (is_there_carryover?, first_digit_of_sum)
    F = lambda a, b : tuple(map(str, divmod(int(a[0]) + int(b[0]) + int(b[1]), 10)))
    """
    starting from (0,0) we process each pair of digits in num1 and num2 and for each pair
    the add starts from the least significant digit, so we need to reverse the inputs (and at the end reverse the output)
    each element in A will represent the sum of the two elements and if there is a carry over 
    """
    A = list(accumulate(zip_longest(reversed(num1), reversed(num2), fillvalue='0'), func = F, initial= ('0','0')))
    """
    for "98" + "7" = "105" A should be [('0', '0'), ('1', '5'),            ('1', '0')]
        initial element which will be ignored ^  Carry^    ^ digit   carryover^.  ^ digit       
    """
    """
    finally we need to extract the digits (which are the second elements in each pair in A (ignoring the first element))
    check if there is a finall carry over (if A[-1][0]=='1') and add a "1" if needed
    and reverse the whole thing
    """
    return ("1" if A[-1][0]=='1' else "") + "".join(list(zip(*A[:0:-1]))[1])


if __name__ == '__main__':
    # print(addStrings('31','29'))
    print(addStrings_alt('31','29'))
    print(addStrings_alt('1','9'))
    print(addStrings_alt('0','0'))
    print(addStrings_alt('1','99'))
