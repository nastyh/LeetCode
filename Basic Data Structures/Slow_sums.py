"""
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number:
Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal to the value
of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the list into [1, 5, 4, 5]
and incur a penalty of 5. The goal in this problem is to find the worst possible penalty for a given input.
"""
import heapq
def getTotalTime(arr):  # O(NlogN) both to create a heap and then re-add elements to it
  """
  Maintain a max heap. While it has more than one element:
  take out two element, sum them together, add the sum to res and re-insert into the heap
  """
  h = []
  res = 0
  for num in arr:
    heapq.heappush(h, -num)
  while len(h) > 1:
    curr_sum = 0
    curr_sum += -heapq.heappop(h)
    curr_sum += -heapq.heappop(h)
    heapq.heappush(h, -curr_sum)
    res += curr_sum
  return res


if __name__ == '__main__':                                                 
    print(getTotalTime([4, 2, 1, 3]))
    print(getTotalTime([1, 2, 3, 4, 5]))
  