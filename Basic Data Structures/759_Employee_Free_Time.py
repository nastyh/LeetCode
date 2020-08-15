def employeeFreeTime(schedule):
    # s = sorted(schedule, key = lambda x: x[0])
    ints = sorted([i for s in schedule for i in s], key=lambda x: x[0])
    res = []
    for ix in range(1, len(ints)):
        curr = []
        if ints[ix][0] > ints[ix - 1][1]:
            curr.append(ints[ix - 1][1])
            curr.append(ints[ix][0])
            res.append(curr)
    return res


if __name__ == '__main__':
    print(employeeFreeTime([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]))
    print(employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))
