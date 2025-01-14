
def min_cost_to_sort(arr):
    """
    O(n^2) selection sort
    O(n) result
    Given an array, Find the Minimum Cost to Sort Ascendingly or Descendingly along its length.
    Cost is defined as: MOD(New Value-Orig Value) of the element.
    """
    def selection_sort(arr, reverse=False):
        n = len(arr)
        result = arr[:]
        for i in range(n):
            # Find the minimum or maximum element in the unsorted portion
            target_index = i
            for j in range(i + 1, n):
                if (not reverse and result[j] < result[target_index]) or (reverse and result[j] > result[target_index]):
                    target_index = j
            # Swap the found element with the current element
            result[i], result[target_index] = result[target_index], result[i]
        return result

    n = len(arr)
    
    # Sort the array in ascending and descending order
    ascending = selection_sort(arr, reverse=False)
    descending = selection_sort(arr, reverse=True)
    
    # Calculate the costs
    cost_asc = sum(abs(arr[i] - ascending[i]) for i in range(n))
    cost_desc = sum(abs(arr[i] - descending[i]) for i in range(n))
    
    # Return the minimum cost
    return min(cost_asc, cost_desc)

