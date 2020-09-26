def numberOfSteps(num):  # straightforward
    res = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
            res += 1
        else:
            num -= 1
            res += 1
    return res

def numberOfSteps_binary(num):
    steps = 0
    #Remove the "0b"
    binary = bin(num)[2:]
    """
    The logic is the following: when the number is odd, its binary representation ends with a 1. When you subtract 1 from this number,
    its last byte becomes 0.
    When the number is even, its binary representation ends with a 0. When you divide this number by 2, you remove the last byte.
    So you want to reiterate over 'binary'
    If you see a 1, add 2, otherwise add 1
    You'll overcount for the last byte, so subtract 1 
    """
    steps += sum([2 if bit == '1' else 1 for bit in binary])
    # for bit in binary:
    #     if bit == "1":
    #         steps = steps + 2 # Then it'll take 2 to remove.
    #     else:
    #         steps = steps + 1 # Then it'll take 1 to remove.
    return steps - 1


if __name__ == '__main__':
    print(numberOfSteps(14))  
    print(numberOfSteps(8))    
    print(numberOfSteps_binary(14))  
    print(numberOfSteps_binary(8))   
    