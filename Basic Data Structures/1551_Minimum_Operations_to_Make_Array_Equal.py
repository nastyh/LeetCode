def minOperations(n):  # O(N) and O(1)
    """
    The sum of a sequence of add numbers with n elements = n^2.
    THe min # of operatsion is a sum (n - 1) + (n - 3) + (n - 5) +...+ 1 (or 0)
    """
    res = 0
    # compute the sum:
    # (n - 1) + (n - 3) + (n - 5) + ... + 1 (or 0) 
    while n > 0:
        res += n - 1
        n -= 2
    return res 


def minOperations_1_line(n):
    return (n // 2) * (n // 2 + n % 2)


def minOperations_median(n):  # O(N) both 
    """
    The middle element is the best candidate to change every other element.
    If there are an even number of numbers in the list, change every element to the average of the two middle elements 
    """
    output = 0
    if n == 1:
        return output
    arr = []
    for i in range(n):
        arr.append(2 * i + 1)
    if n % 2 == 0:
        output += 1     # middle 2 guys
        middle = arr[n//2] - 1   # given every two elements are separated by 2 numbers, middle would just be bigger number minus 1.
        for j in range(n//2 + 1, n):
            output += arr[j] - middle
    else:
        middle = arr[n//2]
        for j in range(n // 2 + 1, n):
            output += arr[j] - middle
    return output