"""
For a given integer, add it with the reverse of the value.
Also, check if it is a palindrome. If it is not a palindrome, repeat the process until the sum becomes a palindrome.
Print out the value of the final palindrome and the number of iterations too.
"""
def reverse_and_add(n):
    """
    O(k*d) k num of iterations, d -- num of digits in the curr number
    O(d) space 
    for some numbers (known as Lychrel number candidates), the process may not converge to a palindrome in a reasonable amount of time.
    """
    def reverse_number(n):
        return int(str(n)[::-1])
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]
    
    iterations = 0
    while not is_palindrome(n):
        n = n + reverse_number(n)
        iterations += 1
    return n, iterations
