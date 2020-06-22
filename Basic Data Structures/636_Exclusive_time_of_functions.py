def exclusiveTime(n, logs):
    total = [0 for i in range(n)]
    s = []
    i = 0
    curTime = 0
    while( i < len(logs)):
        curLog = logs[i].split(":")
        curId = int(curLog[0])
        status = curLog[1]
        nextTime = int(curLog[2])
        if (status ==  "start"):
            if (s):
                total[s[-1]]+= nextTime - curTime
            s.append(curId)
            curTime = nextTime
        else:
            total[s[-1]]+= nextTime - curTime + 1
            s.pop()
            curTime = nextTime + 1
        i+=1
    return total