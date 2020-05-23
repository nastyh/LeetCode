import math
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


if __name__ == '__main__':
    print(kClosest([[1,3],[-2,2]], 1))
