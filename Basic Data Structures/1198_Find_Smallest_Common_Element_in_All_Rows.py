def smallestCommonElement(mat):  # O(rc) both
    """
    Brute force: just do d = {element: number of times it appears}
    Then iterate over the dictionary and return the key for which its value == len(mat)
    """
    d = {}
    for el in mat:
        for i in el:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

    if len(mat) not in d.values():
        return -1
    else:
        return [k for k,v in d.items() if v == len(mat)][0]


def smallestCommonElement_bin_search(mat):  # O(mnlogm) m elements in the first row, then binary search n times over m elements. Space O(1)
    """
    Take every element from the first row and look for this element in all other rows using binary search
    If we find, return immediately 
    """
     def binary_search(arr, target):
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid] == target: return True
            elif arr[mid] > target: 
                end = mid - 1
            else: start = mid + 1
        return arr[start] == target

    first = mat[0]
    for val in first:
        flag = True
        for i in range(1, len(mat)):
            arr = mat[i]
            if not binary_search(arr, val):
                flag = False
                break
        if flag: return val
    return -1


if __name__ == '__main__':
    print(smallestCommonElement([[1, 2, 3,4, 5],[2, 4, 5, 8, 10],[3, 5, 7, 9, 11],[1, 3, 5, 7, 9]]))
    print(smallestCommonElement_bin_search([[1, 2, 3, 4, 5],[2, 4, 5, 8, 10],[3, 5, 7, 9, 11],[1, 3, 5, 7, 9]]))
