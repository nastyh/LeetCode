def minTimeToVisitAllPoints(points):  # O(n)
	steps = 0
	for i in range(len(points)-1):
		point = points[i]
		next_point = points[i+1]
		steps += max(abs(next_point[0] - point[0]), abs(next_point[1] - point[1]))
	return steps


if __name__ == '__main__':
    print(minTimeToVisitAllPoints([[1, 1],[3, 4],[-1, 0]]))
    print(minTimeToVisitAllPoints([[3, 2],[-2, 2]]))