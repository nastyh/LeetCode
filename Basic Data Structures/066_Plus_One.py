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



if __name__ == '__main__':
    print(plusOne([1,9,9]))
    print(plusOne_alt([1,9,9]))


