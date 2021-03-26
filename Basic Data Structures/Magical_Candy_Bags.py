"""
You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

N = 5 
k = 3
arr = [2, 1, 7, 4, 2]
output = 14
In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
In total you can eat 7 + 4 + 3 = 14 pieces of candy.
"""
import heapq
def maxCandies(arr, k):  # O(hlogh) both 
  """
  Need to maintain a max heap in order to eat the largest bag.
  Accurately with adding the leftovers back: first // by 2 and then apply a minus sign. 
  It's because (-7 // 2) = -4 while (7 // 2) = 3
  """
  h = []
  res = 0
  for num in arr:
    heapq.heappush(h, -num)
  while k > 0:
    curr_piece = 0
    curr_piece = -heapq.heappop(h)
    res += curr_piece
    heapq.heappush(h, -(curr_piece // 2))
    k -= 1
  return res


if __name__ == '__main__':   
    print(maxCandies([2, 1, 7, 4, 2], 3))
    print(maxCandies( [19, 78, 76, 72, 48, 8, 24, 74, 29], 3))