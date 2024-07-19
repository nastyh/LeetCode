from random import randint
 
 
# Generate random numbers between 1 and 12 with equal probability using a
# function that generates random numbers from 1 to 6 with equal probability
def generate():
    """
    x * 2 returns an even random number between 2 and 12
    y & 1 returns 0 if y is even, and 1 if y is odd
    (x * 2) - (y & 1) returns random numbers from 1 to 12 w/ equal prob
    If y & 1 is 0, the expression returns the random even numbers 2, 4, 6, 8, 10, and 12 with equal probability.
    If y & 1 is 1, the expression returns the random odd numbers 1, 3, 5, 7, 9, and 11 with equal probability.
    """
    # generate two random numbers from 1 to 6 with equal probability
    x = randint(1, 6)
    y = randint(1, 6)
 
    return 2*x - (y & 1)