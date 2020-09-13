def insert(intervals, newInterval):
    res, t  = [], 0
    for interval in intervals:
        if newInterval[0] > interval[1]: # adding everything to the left
            res.append(interval)

        elif interval[0] > newInterval[1]:
            break
        else:
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

        t += 1

        res.append(newInterval)
        return res + intervals[t:] if t < len(intervals) else res
        # takes care of the situation when we still have elements on the right that need to be in the result


# another possible to understand

def insert_alt(intervals, newInterval):
    ln = len(intervals)
    output = []
    if ln == 0:
        return [newInterval]

    s, e = newInterval[0], newInterval[1]

    i = 0
    #add intervals before s
    while i < ln and s > intervals[i][0]:
        output.append(intervals[i])
        i += 1

    if not output or output[-1][1] < s:
        output.append(newInterval)
    else:
        #already s is greater and output last element start, as in the while condition above
        output[-1][1] = max(output[-1][1], e)


    while i < ln and output[-1][1] >= intervals[i][0]:
        output[-1][1] = max(output[-1][1], intervals[i][1])
        i += 1

    while i < ln:
        output.append(intervals[i])
        i += 1

    return output

def insert_linear(intervals, newInterval):
    res = []
    intervals.sort(key = lambda x: x[0])

    for n, interval in enumerate(intervals):
        if interval[1] < newInterval[0]:
            res.append(interval)
        elif not (newInterval[1] < interval[0]):
            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])
        else:
            res.append(newInterval)
            return res + intervals[n:]
    return res + [newInterval]

    # long and stupid:
    # new_start, new_end = newInterval
    # idx, n = 0, len(intervals)
    # output = []

    # # add all intervals starting before newInterval
    # while idx < n and new_start > intervals[idx][0]:
    #     output.append(intervals[idx])
    #     idx += 1

    # # add newInterval
    # # if there is no overlap, just add the interval
    # if not output or output[-1][1] < new_start:
    #     output.append(newInterval)
    # # if there is an overlap, merge with the last interval
    # else:
    #     output[-1][1] = max(output[-1][1], new_end)

    # # add next intervals, merge with newInterval if needed
    # while idx < n:
    #     interval = intervals[idx]
    #     start, end = interval
    #     idx += 1
    #     # if there is no overlap, just add an interval
    #     if output[-1][1] < start:
    #         output.append(interval)
    #     # if there is an overlap, merge with the last interval
    #     else:
    #         output[-1][1] = max(output[-1][1], end)
    # return output

def insert_another(intervals, newInterval):
    """"
    Possible to understand:
    add everything that doesn't overlap with newInterval from the left. It's done in if.
    add everything that doesn't overlap with newInterval from the right and make newInterval equal to the current interval
    in all other cases, there is an overlap and you need to choose min for the start and max for the end
    """"
    res = []
    if len(intervals) == 0:
        return [newInterval]
    for i in range(len(intervals)):
        if intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
        elif intervals[i][0] > newInterval[1]:
            res.append(newInterval)
            newInterval = intervals[i]
        else:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
    res.append(newInterval)
    return res

if __name__ == '__main__':
    print(insert([[1,3],[6,9]], [2,5]))
    print(insert_alt([[1,3],[6,9]], [2,5]))
    print(insert_linear([[1,3],[6,9]], [2,5]))
    print(insert_another([[1,3],[6,9]], [2,5]))
    print(insert_another([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
