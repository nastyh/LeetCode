def cutWood(arr, k):
    """
    Explanation: we need to cut (a) longest length wood as possible but also satisfy condition (b) where number of longest wood cuts >= k.
First we need to find the longest wood in the array:
Using that longest wood as our cut range, we can do binary search where the middle will be a cut length and divide every wood by middle to check if we can cut every wood with that length. But what is our left for our binary search. Is it 0? No, it should be one. Remember left and right in our binary search is possible cut length not index. The lowest cut can be 1 not 0. We can't cut wood by 0 length.

Now, we can do a binary search:
Now, we will use the middle number as a possible cut length and check if every wood in woods can be cut with that length. We need a helper function for it that loop and checks and returns true if number of woodCuts is <= k:

If helper returns True, we update our result variable. And since we want even longer wood cuts, we move our left pointer in binary to middle+1. Otherwise, we move our right to middle if wood cut was not valid.

    """
    def isValid(cutLen, arr, k):
      # print(cutLen, arr, k)
      count = 0
      for wood in arr:
        if(wood >= cutLen):
          count += wood // cutLen
        else:
          return False
      # print("Count:", count)
      if(count >= k):
        return True

    left = 1
    right = max(arr)
  # print("left-right:", left, right)
    res = 0
    while left < right:
        middle = (left + right) // 2
        if(isValid(middle, arr, k)):
            res = middle
            left = middle + 1
        else:
            right = middle  #

    return res

if __name__ == '__main__':
    print(cutWood([232, 124, 456], 7))
