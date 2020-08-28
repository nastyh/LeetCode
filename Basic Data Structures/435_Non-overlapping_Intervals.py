import math
def eraseOverlapIntervals(intervals):  # don't know what is wrong here
    res = 0
    if len(intervals) <= 1: return res
    intervals.sort(key = lambda x: (x[0], x[1]))
    curr = intervals[0]
    for ix in range(1, len(intervals)):
        if intervals[ix][0] < curr[1]:
            if intervals[ix][1] <= curr[1]:
                res += 1
                ix += 2
            else:
                res += 1 
                ix += 1
            ix += 1
    return res 


def eraseOverlapIntervals_alt(intervals):
    intervals.sort()
    result, prev = 0, -math.inf
    for l, r in intervals:
        if l < prev:
            result += 1
            if r > prev:
                continue
        prev = r
    return result


if __name__ == '__main__':
    print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(eraseOverlapIntervals([[1,2],[2,3]]))
    print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
    print(eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))

    print(eraseOverlapIntervals_alt([[1,2],[2,3],[3,4],[1,3]]))
    print(eraseOverlapIntervals_alt([[1,2],[1,2],[1,2]]))
    print(eraseOverlapIntervals_alt([[1,2],[2,3]]))
    print(eraseOverlapIntervals_alt([[1,100],[11,22],[1,11],[2,12]]))
    print(eraseOverlapIntervals_alt([[0,2],[1,3],[2,4],[3,5],[4,6]]))
