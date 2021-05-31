import heapq
def connectSticks(sticks):  # O(nlogn) and O(n)
    """
    everything into a heap
    Take out two smallest elements and add them to res
    Add the sum of these two elements back to the heap 
    """
    res = 0
    heapq.heapify(sticks)
    while len(sticks) > 1:
        st1 = heapq.heappop(sticks)
        st2 = heapq.heappop(sticks)
        res += st1 + st2
        heapq.heappush(sticks, st1 + st2)
    return res


def connectSticks_brute_force(sticks):  # O(n^2logn) and O(1)
    """
    Same as above but instead of the heap, resort the whole thing and slice it
    TLE 
    """
    res = 0
    while len(sticks) > 1:
        sticks.sort()
        curr_sum = sticks[0] + sticks[1]
        res += curr_sum
        sticks = sticks[2:]
        sticks.insert(0, curr_sum)
    return res 


if __name__ == '__main__':
    print(connectSticks([2, 4, 3]))
    print(connectSticks([1, 8, 3, 5]))
    print(connectSticks([5]))
    print(connectSticks_brute_force([2, 4, 3]))
    print(connectSticks_brute_force([1, 8, 3, 5]))
    print(connectSticks_brute_force([5]))