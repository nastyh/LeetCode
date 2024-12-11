"""
https://leetcode.com/discuss/interview-question/3925477/Uber-OA

Uber HCVs (High Capacity Vehicles) runs across the city of UberLand. UberLand has N stops where the HCVs pickup or drop the passengers.
There Is a network of M bidirectional roads tnat connects various stops. Each road has a particular length attached to it.

The Uber developers have Introduced a weird feature of credits where each stop has some assigned credits c[i] (0<=i<N),
which the HCV can collect when it reaches the stop. These credits are used to travel on a road and number of credits
used for travelling on a road is equal to the length of the road. So a HCV can travel on a road If it has credits equal or more than the length of the road.

You want to travel from a given source stop S (0<=S<N) to a destination stop D (0<=0<N) with minimum distance travelled.

Calculate the minimum distance that you need to travel or return -1 if there is no way possible.
Assume the HCV starts at the source stop S and has credits equal to the credits of S at the start.

Input:

Each test case has several lines.

The first line contains an integer N which represent the number of stops in UberLand.
The second line contains an array C of N Integers which represents credits for each stop.
The third line contains an integer M which represent the number of roads in UberLand.
Then the following M lines each contain three Integers X (0<=X<N) ,Y (0<=-Y<N) ,Z (1<=Z<=100),
which means there is road connecting stops X and Y with length Z where X != Y
Then the last 2 lines contains one Integer respectively, S and D which represent the source and the destination stop.
Constraints:
1<=N<=50
0<=M<=100
0<=C[i]<=100
1<=Length of each road<=100

"""

from heapq import heappush, heappop

class Stop:
  def __init__(self, id, distance, credits):
    self.id = id
    self.distance = distance
    self.credits = credits

  def __lt__(self, other):
    return self.distance < other.distance


min_distances = [[float('inf')] * 101 for _ in range(N)]  # Considering max credits as 100
  min_distances[S][C[S]] = 0

  d = []
  heappush(d, Stop(S, 0, C[S]))

  while d:
    current = heappop(d)

    if current.id == D:
      return current.distance

    for neighbor in graph[current.id]:
      next_stop, road_length = neighbor
      next_credits = current.credits + C[next_stop] - road_length

      if 0 <= next_credits <= 100 and min_distances[next_stop][next_credits] > current.distance + road_length:
        min_distances[next_stop][next_credits] = current.distance + road_length
        heappush(d, Stop(next_stop, min_distances[next_stop][next_credits], next_credits))

  return -1

# Example usage
N = 5  # Number of cities
C = [2, 3, 1, 4, 2]  # Credits at each city
M = 3  # Number of roads
roads = [[0, 1, 1], [1, 2, 2], [2, 4, 1]]  # Roads (city1, city2, road_length)
S = 0  # Starting city
D = 4  # Destination city

min_distance = find_minimum_distance(N, C, M, roads, S, D)
if min_distance == -1:
  print("No path found")
else:
  print(f"Minimum distance: {min_distance}")


