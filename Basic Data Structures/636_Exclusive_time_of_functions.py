def exclusiveTime(n, logs):  # O(n) both
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
                total[s[-1]] += nextTime - curTime  # updating the last value on the fly 
            s.append(curId)
            curTime = nextTime
        else:
            total[s[-1]] += nextTime - curTime + 1
            s.pop()
            curTime = nextTime + 1
        i += 1
    return total


def exclusiveTime_another(n, logs):
    helper = lambda x: (int(x[0]), x[1], int(x[2]))  # to convert id and time to integer
    logs = [helper(x.split(':')) for x in logs]         # convert [string] to [(,,)]
    ans, s = [0] * n, []                                    # initialize answer and stack
    for (i, status, timestamp) in logs:                     # for each record
        if status == 'start':                               # if it's start
            if s: ans[s[-1][0]] += timestamp - s[-1][1]     # if s is not empty, update time spent on previous id (s[-1][0])
            s.append([i, timestamp])                        # then add to top of stack
        else:                                               # if it's end
            ans[i] += timestamp - s.pop()[1] + 1            # update time spend on `i`
            if s:
                    s[-1][1] = timestamp + 1                    # if s is not empty, udpate start time of previous id; 
    return ans



if __name__ == '__main__':
    print(exclusiveTime_another(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))