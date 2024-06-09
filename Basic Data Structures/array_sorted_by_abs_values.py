def sortAbs(arr):
    """
    Given an array sorted by its absolute values, return sorted array by it actually values - Solve in O(N)
    naive, prob not O(n)
    """
    egs, pos = [ele for ele in arr if ele < 0], [ele for ele in arr if ele >= 0]
    return reversed(negs) + pos

def sortAbs_deque(arr):
    """
    traverse the array from left to right and insert the negative elements in the front
    and the positive elements in the back of the deque. Now pop the elements from the front of the deque to fill the array and get the answer.
    """
    dq = []
    for i in range(len(arr)):
        if (arr[i] < 0):
             # Pushing negative elements in
            # the front of the deque
            dq.insert(0, arr[i])
        else:
            dq.append(arr[i])
    return dq

if __name__ == '__main__':
    print(sortAbs_deque([0, -1, 2, -4, 5, 6, -10, -13, -22]))