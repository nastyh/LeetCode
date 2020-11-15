def removeInterval(intervals, toBeRemoved):
    res = []
    for interval in intervals:
        if interval[1] <= toBeRemoved[0] or interval[0] >= toBeRemoved[1]:  # nothing intersects, just add interval to the result
            res.append(interval)
        else:  # otherwise start comparing staring points to each other
            if interval[0] < toBeRemoved[0]:
                res.append([interval[0], toBeRemoved[0]])
            if interval[1] > toBeRemoved[1]:  # and ending points to each other 
                res.append([toBeRemoved[1], interval[1]])
    return res


if __name__ == '__main__':
    print(removeInterval([[0, 2],[3, 4],[5, 7]], [1, 6]))
    print(removeInterval([[0, 5]], [2, 3]))
    print(removeInterval([[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], [-1, 4]))

    