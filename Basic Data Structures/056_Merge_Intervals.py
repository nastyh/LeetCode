def merge(intervals):
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


if __name__ == '__main__':
    # print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4], [2,3]]))
