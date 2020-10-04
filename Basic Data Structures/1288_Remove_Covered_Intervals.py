def removeCoveredIntervals(intervals):
    cnt = 0
    intervals.sort(key = lambda x: (x[0], -x[1]))
    curr_st, curr_end = intervals[0][0], intervals[0][1]
    for interval in intervals[1:]:
        if curr_st <= interval[0] < curr_end and curr_st < interval[1] <= curr_end:
            cnt += 1
        curr_st = interval[0]
        curr_end = max(curr_end, interval[1])
    return len(intervals) - cnt


if __name__ == '__main__':
    print(removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
    print(removeCoveredIntervals([[1, 4], [2, 3]]))
    print(removeCoveredIntervals([[0, 10], [5, 12]]))
    print(removeCoveredIntervals([[3, 10], [4, 10], [5, 11]]))
    print(removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))