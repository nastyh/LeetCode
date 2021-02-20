from collections import counter
def judgeCircle(moves):  # O(n) and O(1)
    l, u = 0, 0
    for ch in moves: 
        if ch == 'L':
            l += 1
        if ch == 'R':
            l -= 1
        if ch == 'U':
            u += 1
        if ch == 'D':
            u -= 1
    return u == l == 0


def judgeCircle_dict(moves):  # O(n) and prob O(1)
    """
    Same but with a dictionary (no need at all)
    """
    lr, up = {'L' : 0}, {'U': 0}
    for ch in moves:
        if ch == 'L':
            lr['L'] += 1
        if ch == 'R':
            lr['L'] -= 1
        if ch == 'U':
            up['U'] += 1
        if ch == 'D':
            up['U'] -= 1
    return sum(v for v in lr.values()) == 0 and sum(v for v in up.values())== 0


def judgeCircle_counter(moves):  # O(n) both
    """
    Kinda Pythonic
    """
    d = Counter(moves)
    return d['L'] - d['R'] == 0 and d['U'] - d['D'] == 0