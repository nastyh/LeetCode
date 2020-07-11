def merge(intervals):
    if len(intervals) == 0:
        return []
    intervals = sorted(intervals, key = lambda x: x[0])
    merged = []
    merged.append(intervals[0])  # [[1;3]] -> [[1,6]]
    for interval in intervals[1:]:

        if interval[0] <= merged[-1][-1]:
            if interval[1] >  merged[-1][-1]:
                merged[-1][-1] = interval[1]
        else:
            merged.append(interval)

    return merged

def merge_m(intervals): # using max instead of if statements, probably looks more professional
    if len(intervals) == 0:
        return []
    intervals = sorted(intervals, key = lambda x: x[0])
    merged = []
    merged.append(intervals[0])
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged


if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge_m([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4], [2,3]]))
    print(merge_m([[1,4], [2,3]]))
