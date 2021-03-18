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


def eraseOverlapIntervals_2_pointers(intervals):  # o(nlogn) and O(1)
    """
    Sort by the start time
    Two pointers: l and r intervals
    Start comparing them
    If the end of the left is <= start of the right, there is no overlap, move both pointers
    if the end of the left is <= end of the right: there is an overlap (b/c we're using elif, the previous case has been taken care of),
    then let's greedily remove the right interval, increment res and move the r pointer
    if the end of the left is > end of the right, it means that the left is larger. We'll remove it, and increment the pointers accordingly 
    """
    intervals.sort()
    res = 0
    l, r = 0, 1 
    while r < len(intervals):
        if intervals[l][1] <= intervals[r][0]:
            l = r 
            r += 1
        elif intervals[l][1] <= intervals[r][1]:
            res += 1
            r += 1
        elif intervals[l][1] > intervals[r][1]:
            res += 1
            l = r
            r += 1
    return res


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
