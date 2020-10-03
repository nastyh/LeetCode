import math
from collections import defaultdict
def maxDistance(arrays):  # two passes
    minidx = maxidx = 0
    for i, val in enumerate(arrays):
        if val[0] < arrays[minidx][0]:
            minidx = i
        if val[-1] > arrays[maxidx][-1]:
            maxidx = i
    if minidx != maxidx:
        return abs(arrays[maxidx][-1] - arrays[minidx][0])
    # overlap, let's do another pass
    twominidx = twomaxidx = (maxidx + 1) % len(arrays)
    for i, val in enumerate(arrays):
        if i == maxidx: continue
        if val[0] < arrays[twominidx][0]: twominidx = i
        if val[-1] > arrays[twomaxidx][-1]: twomaxidx = i
    return max(abs(arrays[twomaxidx][-1] - arrays[minidx][0]), abs(arrays[maxidx][-1] - arrays[twominidx][0]))

def maxDistance_dict(arrays):
    min_d, max_d = defaultdict(list), defaultdict(list)
    res = 0
    for k, v in enumerate(arrays):
        min_d[v[0]].append(k)
        max_d[v[-1]].append(k)
    for i in min_d:
        for j in max_d:
            if abs(j - i) > res:
                if min_d[i] != max_d[j]:
                    res = abs(j - i)
                elif len(min_d[i]) > 1:
                    res = abs(j - i)
    return res



if __name__ == '__main__':
    print(maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
    print(maxDistance([[1, 4], [0, 5]]))
    print(maxDistance_dict([[1, 2, 3], [4, 5], [1, 2, 3]]))
    print(maxDistance_dict([[1, 4], [0, 5]]))