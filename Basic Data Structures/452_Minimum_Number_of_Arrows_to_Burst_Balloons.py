def findMinArrowShots(points):
    if len(points) == 0: return 0
    res = 1
    points.sort(key = lambda x: x[1])
    curr = points[0]
    for i in range(1, len(points)):
        if points[i][0] <= curr[1] <= points[i][1]:
            continue
        else:
            res += 1
            curr = points[i]
    return res


if __name__ == '__main__':
    print(findMinArrowShots([[10, 16],[2, 8],[1, 6],[7, 12]]))
    print(findMinArrowShots([[1, 2],[3, 4],[5, 6],[7, 8]]))
    print(findMinArrowShots([[1, 2],[2, 3],[3, 4],[4, 5]]))