from fractions import Fraction as F, gcd
def mirrorReflection(p, q):
    """
    The initial ray can be described as going from an origin (x, y) = (0, 0) in the direction (rx, ry) = (p, q).
    From this, we can figure out which wall it will meet and where, and what the appropriate new ray will be (based on reflection).
    We keep simulating the ray until it finds it's destination.
    The parameterized position of the laser after time t will be (x + rx * t, y + ry * t).
    From there, we know when it will meet the east wall (if x + rx * t == p), and so on. 
    For a positive (and nonnegligible) time t, it meets the next wall.
    We can then calculate how the ray reflects. If it hits an east or west wall, then rx *= -1, else ry *= -1.
    """
    x = y = 0
    rx, ry = p, q
    targets = [(p, 0), (p, p), (0, p)]

    while (x, y) not in targets:
        #Want smallest t so that some x + rx, y + ry is 0 or p
        #x + rxt = 0, then t = -x/rx etc.
        t = float('inf')
        for v in [gcd(-x,rx), gcd(-y,ry), gcd(p-x,rx), gcd(p-y,ry)]:
            if v > 0: t = min(t, v)
        x += rx * t
        y += ry * t
        #update rx, ry
        if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
            rx *= -1
        if y == p or y == 0:
            ry *= -1
    return 1 if x==y==p else 0 if x==p else 2


def mirrorReflection_math(p, q):
    """
    model it as a straight line through reflections of the room.
    For example, if p = 2, q = 1, then we can reflect the room horizontally, and draw a straight line from (0, 0) to (4, 2).
    The ray meets the receptor 2, which was reflected from (0, 2) to (4, 2).
    In general, the ray goes to the first integer point (kp, kq) where k is an integer, and kp and kq are multiples of p.
    Thus, the goal is just to find the smallest k for which kq is a multiple of p.
    The mathematical answer is k = p / gcd(p, q)
    """
    g = gcd(p, q)
    p = (p / g) % 2
    q = (q / g) % 2
    return 1 if p and q else 0 if p else 2

def mirrorReflection_another(p, q):
    x, y = 0, 0
    while True:
        y += q
        if x == 0:
            x = p
        else:
            x = 0
        if y % p == 0:
            if y / p % 2 == 0:
                return 0
            elif x == p:
                return 1
            else:
                return 2


if __name__ == '__main__':
    print(mirrorReflection(2, 1))
    print(mirrorReflection_math(2, 1))
    print(mirrorReflection_another(2, 1))