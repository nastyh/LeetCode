def minDistance(height, width, tree, squirrel, nuts):
    """
    (a) Distance squirrel travels from it's start position to the first nut.
    (b) 1 times the distance from the first nut to the tree
    (c) 2 times the distance from all the other nuts to the tree
    """
	def manhattan(a,b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])

	res = float('inf')
	dist = [manhattan(n, tree) for n in nuts] # Distance from each nut to the tree
	total = sum(dist)
	all_except = [total - d for d in dist]      # Sum of distance to tree for all nuts except for nuts[i] (the starting nut)
	# Try choosing each nut as the "starting nut" and calculate the total distance
	for i in range(len(nuts)):
		a = manhattan(squirrel, nuts[i])
		b = dist[i]
		c = 2 * all_except[i]
		res = min(res, a + b + c)
	return res


def minDistance_alt(height, width, tree, squirrel, nuts):
    def _helper(ptA, ptB):
        xA, yA = ptA
        xB, yB = ptB
        return abs(xA - xB) + abs(yA - yB)
    
    total, d = 0,  float('inf')
    for nut in nuts:
        dTN = _helper(tree, nut)
        dSN = _helper(squirrel, nut)
        total += dTN
        d = min(d, dSN - dTN)
    return 2 * total + d