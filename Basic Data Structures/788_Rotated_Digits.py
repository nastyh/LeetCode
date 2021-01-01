def rotatedDigits(N):
    """
    Brute force approach.
    Go element by element. If it's a single digit, then make sure it's not in rotated_themselves or in invalid and increment res
    If it's a double- or more-digit number, we use a helper function. It takes a number and turns it into a list of digits (like 410 becomes [4, 1, 0])
    Then we go through the list and create a new list rotating every digit according to the rules.
    If the new list isn't the same as the provided list, increment res 
    """
    rotated_all = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}
    rotated_themselves = [0, 1, 8]
    invalid = [3, 4, 7]
    res = 0
    nums = [i for i in range(1, N + 1)]
    def _helper(number):
        l = []
        while number > 0:
            l.append(number % 10)
            number //= 10
        return l[::-1]
    for num in nums:
        if num <= 9:
            if num in invalid or num in rotated_themselves:
                continue
            else:
                res += 1
        else:
            big_number = _helper(num)
            if any(i in invalid for i in big_number):
                continue
            rotated_big_number = []
            for i in big_number:
                rotated_big_number.append(rotated_all[i])
            if rotated_big_number != big_number:
                res += 1
    return res


def rotatedDigits_alt(N):
    res = 0
    for d in range(1, N + 1):
        d = str(d)
        if '3' in d or '4' in d or '7' in d:
            continue
        if '2' in d or '5' in d or '6' in d or '9' in d:
            res += 1
    return res
                
        