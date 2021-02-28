from collections import Counter
import heapq
def leastInterval(tasks, n):  # O(nlogn) b/c of sorting and O(n)
    """
    build a dict task: frequencies and sort it 
    """
    char_freq = sorted(Counter(tasks).values() , reverse = True) 
    ix, counter, max_freq = 0, 0 ,char_freq[0]
    while ix < len(char_freq) and char_freq[ix] == max_freq:
        counter += 1
        result = (max_freq - 1) * (n + 1) + counter
        ix += 1
    return max(result, len(tasks))


def leastInterval_alt(tasks, n):
    # create list of process occurances
    occurances = list(Counter(tasks).values())

    # base interval calculation = # of groups * size of each group
    intervals = (max(occurances) - 1) * (n + 1)
    # account for remaining intervals from processes with most occurances
    count_procc_with_max = occurances.count(max(occurances))
    # add these to your total interval count
    intervals += count_procc_with_max

    # return max of calculated intervals and length of initials task list
    return max(intervals, len(tasks))


def leastInterval_heap(tasks, n):  #O(nlogn) b/c of heap and O(n)
    d = Counter(tasks)
    h = [-v for v in d.values()]
    heapq.heapify(h)
    res = 0
    while len(h) > 0:
        time = 0
        tmp = []
        for i in range(n + 1):
            if len(h) > 0:
                tmp.append(-heapq.heappop(h) - 1)
                time += 1
        for t in tmp:
            if t > 0:
                heapq.heappush(h, -t)
        if len(h) == 0:
            res += time
        else:
            res += n + 1
    return res

if __name__ == '__main__':
    print(leastInterval(["A","A","A","B","B","B"], 2))
    print(leastInterval_alt(["A","A","A","B","B","B"], 2))
    print(leastInterval_heap(["A","A","A","B","B","B"], 2))
