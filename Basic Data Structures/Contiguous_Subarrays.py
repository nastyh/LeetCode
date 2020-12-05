def count_subarrays(arr):
  # Write your code here
  n = len(arr)
  result = [n] * n
  st = []
  for i, x in enumerate(arr):
      while st and x >= arr[st[-1]]:
          result[st.pop()] -= n-i
      st.append(i)
  st.clear()
  for i, x in reversed(list(enumerate(arr))):
      while st and x >= arr[st[-1]]:
          result[st.pop()] -= i+1
      st.append(i)
  return result