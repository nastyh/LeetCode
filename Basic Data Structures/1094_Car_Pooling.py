from collections import defaultdict
def carPooling_dict(trips, capacity):
    trip_capacity = defaultdict(int)
    for i in range(len(trips)):
        no = trips[i][0]
        start = trips[i][1]
        dest = trips[i][2]
        for j in range(start,dest):
            trip_capacity[j] += no
            if trip_capacity[j] > capacity:
                return False
    return True


def carPooling_greedy(trips, capacity):
    starts = sorted([(trip[1], trip[0]) for trip in trips])
    ends = sorted([(trip[2], trip[0]) for trip in trips])
    pax = st = en = 0
    while st < len(trips):
        if starts[st][0] < ends[en][0]:
            pax += starts[st][1]
        else:
            pax -= ends[en][1]
            en += 1
            continue
        st += 1
        if pax > capacity:
            return False
    return True

if __name__ == '__main__':
    print(carPooling_dict([[2, 1, 5],[3, 3, 7]], 4))
    print(carPooling_dict([[2, 1, 5],[3, 3, 7]], 5))
    print(carPooling_dict([[2, 1, 5],[3, 5, 7]], 3))
    print(carPooling_dict([[3, 2, 7],[3, 7,9], [8, 3, 9]], 11))
    print(carPooling_greedy([[2, 1, 5],[3, 3, 7]], 4))
    print(carPooling_greedy([[2, 1, 5],[3, 3, 7]], 5))
    print(carPooling_greedy([[2, 1, 5],[3, 5, 7]], 3))
    print(carPooling_greedy([[3, 2, 7],[3, 7,9], [8, 3, 9]], 11))