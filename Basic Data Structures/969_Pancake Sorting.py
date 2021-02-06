def pancakeSort(A):  # O(n^2) and O(n)
    """
    Need to get the max element to the right of the list
    find the max element
    Move this element to the beginning
    Reverse the whole thing so that this largest element is all the way to the right
    Don't longer consider it in further analysis. Then process the rest of the list in a similar fashion
    """
    x = len(A)
    res = []
    for ix in range(x):
        max_val = max(A[:x - ix])
        max_val_ix = A.index(max_val) + 1
        A[:max_val_ix] = reversed(A[:max_val_ix])
        res.append(max_val_ix)

        A[:x - ix] = reversed(A[:x - ix])
        res.append(x - ix)
    return res
