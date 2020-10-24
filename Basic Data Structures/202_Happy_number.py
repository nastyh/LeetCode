def isHappy(n):  # extra space 
    seen = set()
    while n != 1:
        current = n
        sum_var  = 0
        while current != 0:
            sum_var += (current % 10) ** 2
            current = current // 10
        if sum_var in seen:
            return False
        else:
            seen.add(sum_var)
            n = sum_var
    return True


def isHappy_alt(n):  # no extra space
    def numSquareSum(n): 
        squareSum = 0; 
        while n: 
            squareSum += (n % 10) * (n % 10); 
            n = int(n / 10); 
        return squareSum
    slow = n; 
    fast = n; 
    while(True): 
    # move slow number 
    # by one iteration 
        slow = numSquareSum(slow)
    # move fast number 
    # by two iteration 
        fast = numSquareSum(numSquareSum(fast))
        if(slow != fast): 
            continue
        else: 
            break

# if both number meet at 1,  
    #then return true 
    return (slow == 1); 


if __name__ == '__main__':
    print(isHappy(19))
    print(isHappy_alt(19))