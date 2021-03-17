import math, random
class Solution:
    """
    Uniformly choose a point in the circle area and find the distance between this point and the center using polar coordinates
    """

    def __init__(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center
        self.area = math.pi * radius ** 2

    def randPoint(self):
        theta = 2 * math.pi * random.random()  # angle between a line connecting (0, 0) and a random point (x, y) and the x axis
        R = math.sqrt(random.uniform(0, self.area) / math.pi)
        return [self.x + R * math.cos(theta), self.y + R * math.sin(theta)]


class Solution_another:

	def __init__(self, radius, x_center, y_center):
		self.radius = radius
		self.xc = x_center
		self.yc = y_center

	def randPoint(self):
		while True:
			rx = (random.random() - 0.5) * 2
			ry = (random.random() - 0.5) * 2
			
			if ((rx**2) + (ry**2)) <= 1:
				break

		return [rx * self.radius + self.xc, ry * self.radius + self.yc]