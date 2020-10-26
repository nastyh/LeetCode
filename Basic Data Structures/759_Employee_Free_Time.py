def employeeFreeTime(schedule):
    # s = sorted(schedule, key = lambda x: x[0])
    ints = sorted([i for s in schedule for i in s], key=lambda x: x[0])  # flatten the list
    res = []
    for ix in range(1, len(ints)):
        curr = []
        if ints[ix][0] > ints[ix - 1][1]:
            curr.append(ints[ix - 1][1])
            curr.append(ints[ix][0])
            res.append(curr)
    return res


def employeeFreeTime_alt(schedule):  # same idea but with an implementation for the weird Leetcode 
     schedule2 = []
        for x in schedule: 
            for y in x:  
                schedule2.append([y.start, y.end])
        schedule2.sort(key = lambda x: x[0])
        start, end = schedule2[0][0], schedule2[0][1]  
        res = []  
        for i in range(1, len(schedule2)):  
            if schedule2[i][0] <= end:
                end = max(end, schedule2[i][1])
            else:
                res.append([start, end])
                start, end = schedule2[i][0], schedule2[i][1]
        res.append([start, end])
        ans = []
        
        for i in range(len(res)-1):
            ans.append(Interval(res[i][1], res[i+1][0]))
        return ans


if __name__ == '__main__':
    print(employeeFreeTime([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]))
    print(employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))
