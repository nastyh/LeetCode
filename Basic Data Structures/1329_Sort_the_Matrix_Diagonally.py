from collections import defaultdict
import heapq
def diagonalSort_dict(mat):  # O(NM*log(min(N, M))) and space O(min(N, M)) used by the list with diagonal elements 
    """
    collect values into a list of list where a key is the difference between rows and cols
    Elements on the same diagonal will be together as a result
    Then sort each diagonal using in-built sort and push the results back
    """
    d = defaultdict(list)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            d[i - j].append(mat[i][j])
    for i in d.keys():
        if i < 0:
            y = 0
            x =- i
        else:
            y = i
            x = 0
        li = d[i]
        li.sort()
        while y < len(mat) and x < len(mat[0]):
            mat[y][x] = li.pop(0)
            x += 1
            y += 1
    return mat


def diagonalSort_heap(mat):  # O(NM * logn(min(N, M))) and O(NM) to keep the hashmap
    """
    Again start with a list of list
    But every list will be a heap
    Then just start another double loop and for every element pop a value from a respective key-value par in d
    """
    d = defaultdict(list)
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            heapq.heappush(d[row - col], mat[row][col])
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            mat[row][col] = heapq.heappop(d[row - col])
    return mat


if __name__ == '__main__':
    print(diagonalSort_dict([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
    print(diagonalSort_heap([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))