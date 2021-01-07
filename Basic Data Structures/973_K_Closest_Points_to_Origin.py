import math, heapq, random
def kClosest(points, K):
    if K > len(points):
        return None
    res, curr_res = [], 0
    for point in points:
        curr_res = math.sqrt( (0 - point[0])**2 + (0-point[1])**2 )
        res.append(curr_res)
    comb = zip(points, res)

    sorted_comb = sorted(comb, key = lambda x: x[1])
    values_back = [a for a, b in sorted_comb]
   # values_back = [a for a, b in sorted(comb, key = lambda x: x[1])] # one liner
    return values_back[:K]


def kClosest_alt(points, K):  # O(nlogK) b/c logK to put and klogk to extract; space O(nlogK)
    if K > len(points):
        return None
    res, curr_res = [], []
    for point in points:
        heapq.heappush(curr_res, (math.sqrt( (0 - point[0])**2 + (0-point[1])**2 ), point))
    res = []
    for i in range(K):
        res.append(heapq.heappop(curr_res)[1])
    return res


def kClosest_heap_zip(points, K): 
    """
    Same as above with a slightly clearer addition of combined to the heap
    """
    distances, h, res = [], [], []
    for point in points:
        curr_res = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
        distances.append(curr_res)
    combined = zip(distances, points)
    for i in combined:
        heapq.heappush(h, i)
    # heapq.heappush(h, [i for i in combined])  # for some reason won't work, so had to resort to the for statement above
    for _ in range(K):
        d, p = heapq.heappop(h)  # unpacks into distance and point
        res.append(p)
    return res


def kClosest_div_and_conq(points, K):
    dist = lambda i: points[i][0]**2 + points[i][1]**2

    def sort(i, j, K):
        # Partially sorts A[i:j+1] so the first K elements are
        # the smallest K elements.
        if i >= j: return
        # Put random element as A[i] - this is the pivot
        k = random.randint(i, j)
        points[i], points[k] = points[k], points[i]
        mid = partition(i, j)
        if K < mid - i + 1:
            sort(i, mid - 1, K)
        elif K > mid - i + 1:
            sort(mid + 1, j, K - (mid - i + 1))
    def partition(i, j):
        # Partition by pivot A[i], returning an index mid
        # such that A[i] <= A[mid] <= A[j] for i < mid < j.
        oi = i
        pivot = dist(i)
        i += 1
        while True:
            while i < j and dist(i) < pivot:
                i += 1
            while i <= j and dist(j) >= pivot:
                j -= 1
            if i >= j: break
            points[i], points[j] = points[j], points[i]

        points[oi], points[j] = points[j], points[oi]
        return j
    sort(0, len(points) - 1, K)
    return points[:K]



if __name__ == '__main__':
    # print(kClosest([[1, 3],[-2, 2]], 1))
    # print(kClosest_alt([[1, 3],[-2, 2]], 1))
    # print(kClosest_heap_zip([[1, 3],[-2, 2]], 1))
    print(kClosest_heap_zip([[3, 3],[5, -1], [-2, 4]], 2))
    # print(kClosest_div_and_conq([[1, 3],[-2, 2]], 1))
