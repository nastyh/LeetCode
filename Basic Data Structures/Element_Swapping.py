def findMinArray(arr, k):
  # Write your code here
  for i in range(len(arr) - 1):
    # Set the position where we we want 
    # to put the smallest integer 
        pos = i 
        for j in range(i + 1, len(arr)): 
            # If we exceed the Max swaps 
        # then terminate the loop 
            if (j-i > k): 
                break
  
            # Find the minimum value from i+1 to 
            # max (k or n) 
            if (arr[j] < arr[pos]): 
                pos = j 
  
        # Swap the elements from Minimum position 
        # we found till now to the i index 
        for j in range(pos, i, - 1): 
            arr[j],arr[j - 1] = arr[j -1 ], arr[j] 
  
        # Set the final value after swapping pos-i 
        # elements 
        k -= pos - i
  return arr