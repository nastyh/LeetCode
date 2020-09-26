def findPoisonedDuration(timeSeries, duration):
    res = 0
    if len(timeSeries) == 0: return res
    if len(timeSeries) == 1: return duration
    for ix in range(len(timeSeries) - 1):
        if timeSeries[ix + 1] - timeSeries[ix] >= duration:
            res += duration
        else:
            res += timeSeries[ix + 1] - timeSeries[ix]
    res += duration
    return res


if __name__ == '__main__':
    print(findPoisonedDuration([1, 4], 2))
    print(findPoisonedDuration([1, 2], 2))