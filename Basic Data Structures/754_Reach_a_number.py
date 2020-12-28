import math
def reachNumber(target):  # O(sqrt(target)) and O(1)
    target = abs(target)
    k = 0
    while target > 0:
        k += 1
        target -= k
    return k if target % 2 == 0 else k + 1 + k%2


def reachNumber_alt(number):
    """
    If d is even, we can set the d/2 step in opposite direction, so that 1+2+...-d/2 +... + k = target. so the min is k.
    If d is odd, it means target cannot be reached in k steps, because any opposition of the k steps changes the gap evenly.
    So there are two cases: (1) if the gap between target and 1+2+...+(k+1) is even, we can set some step in opposite direction so that target can be reached.
    This results in a (k+1) sequence. (2) if the gap is odd, as the same reason, no sequence with k+1 steps exists. and a sequence with k+2 steps always
    exists byreversing some steps to get (target-1) in k steps, and spending 2 extra moves in opposite direction to get target.
    """
    t = abs(target)
    n = math.ceil((math.sqrt(8 * t + 1) - 1) / 2)
    d = n * (n + 1) / 2 - t
    if d % 2 == 0:
        return n
    elif (d + n + 1) % 2 == 0:
        return n + 1
    else:
        return n + 2