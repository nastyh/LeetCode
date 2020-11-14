def validSquare(p1, p2, p3, p4):
    """
    find the 6 sides formed by the points, and then store them in len_side.
    count the sides in len_side and store the nums in side_num.
    check whether the counts in side_num are 4 and 2, which means we have four and two same sides respectively.
    """
    vertices=[p1,p2,p3,p4]
    len_side=[]
    for i in range(3):
        for j in range(i+1,4):
            len_side.append(sqrt((vertices[i][0]-vertices[j][0])**2+(vertices[i][1]-vertices[j][1])**2))
    not_overlap=set(len_side)
    side_num=[]
    for item in not_overlap:
        side_num.append(len_side.count(item))
    ##### if it's valid square, it must have same side-len num like 4 and 2
    if (4 in side_num) and (2 in side_num):
        return True
    else:
        return False

def validSquare_alt(p1, p2, p3, p4):
    """
    4 points have to be different, otherwise return False
    Find distance from point A to all other 3 points, add to a dictionary
    For each point X, the distance to 3 other points should satisfy following conditions
    Distance to its left neighbor (call it d_left) and right neighbour (call it d_right) should be the same
    d_left = sqrt( (X[1]-left[1]) ** 2 + (X[0] - left[0]) ** 2)
    d_left ** 2 + d_right ** 2 == distance_to_the_point_on_the_other_side_of_diagnal ** 2 (Pythagoras theorem)
    If any of the 2 conditions above failed, then it's not a square
    Return True if all above conditions are hold
    """
    if not p1 != p2 != p3 != p4: return False
    dis = lambda x, y: (y[1]-x[1])**2 + (y[0]-x[0])**2   # lambda function to calc hypothenus
    points = [p1, p2, p3, p4]
    d = collections.defaultdict(list)
    for i in range(4):                                   # calculate distance between each points to other 3
        for j in range(i+1, 4):
            distance = dis(points[i], points[j])
            d[tuple(points[i])].append(distance)
            d[tuple(points[j])].append(distance)
    for point, distances in d.items():                   # check neighbors's edges equality & Pythagoras theorem
        distances.sort()
        if not (distances[0] == distances[1] and sum(distances[:2]) == distances[2]): return False
    return True