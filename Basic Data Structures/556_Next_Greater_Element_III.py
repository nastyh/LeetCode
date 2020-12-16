 def nextGreaterElement(n):
    """
    :type n: int
    :rtype: int
    """
    a = list(str(n))
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i < 0:
        return -1
    j = len(a) - 1
    while j >= 0 and a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    r = a[:i+1] + a[len(a)-1:i:-1]
    res = int(''.join(r))
    return res if res < 2**31-1 else -1


def nextGreaterElement_alt(n):
    str_n = str(n)
    digits = [int(i) for i in list(str_n)]

    # find the point at which to begin swap, go from right to left to find the first point of violation
    ptr = len(digits) - 1
    while ptr >= 1:
        if digits[ptr - 1] < digits[ptr]:
            break
        else:
            ptr-=1
    if ptr==0:
        return -1
    # Violation is at ptr-1, now, find exactly once, the first occurrence of next largest element to replace with
    largest_till_now = ptr
    for i in range(ptr + 1, len(digits)):
        if digits[i]>digits[ptr - 1] and digits[i] < digits[largest_till_now]:
            largest_till_now = i
    digits[ptr - 1], digits[largest_till_now] = digits[largest_till_now], digits[ptr - 1]

    # now, make sure that this is indeed the next smallest
    # to do so, sort the remaining elements from ptr onwards
    digits[ptr:] = sorted(digits[ptr:])
    result = int(''.join([str(i) for i in digits]))
    # finally, check if this satisfies the bit constraint
    if result.bit_length() < 32:
        return result
    else:
        return -1

    
def nextGreaterElement_another(n):
    n1 = list(str(n))
    s = ""
    for i in range(len(n1) - 1,0,-1):      #iterating in reverse order
        if n1[i] > n1[i - 1]:   #finding an element bigger than its previous element
            first = n1[:i]   #first part (we will something about that last element)
            second = sorted(n1[i:])   # second part needs to be sorted
            for i in range(len(second)):
                if second[i] > first[-1]:   # finding element in second part such that it greater than last element inn first
                    first[-1], second[i] = second[i], first[-1] #swap them
                    break
            first = first + second
            for i in first:
                s += i
            break
    if s == "" or int(s) > 2147483647: #calculating (2**31)-1 consumes time
        return -1
    return s