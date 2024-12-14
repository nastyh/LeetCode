"""
Manual implementation of the Python functions
"""
def bisect_left(nums, x):
  """
  Return the leftmost index where x could be inserted in list a while maintaining sorted order.
  Args:
    a: The sorted list.
    x: The value to be inserted.

  Returns:
    The leftmost index where x could be inserted.
  """
  l, r = 0, len(nums)
  
  while l < r:
    mid = l + (r - l) // 2
    if nums[mid] < x:
      l = mid + 1
    else:
      r = mid
  return l

def bisect_right(nums, x):
  """
  Return the rightmost index where x could be inserted in list a while maintaining sorted order.

  The list must be sorted (non-decreasing) beforehand.
    x: The value to be inserted.
  Returns:
    The rightmost index where x could be inserted.
  """
  l, r = 0, len(nums)
  while l < r:
    mid = l + (r - l) // 2
    if x < nums[mid]:
      l = mid
    else:
      l = mid + 1
  return l