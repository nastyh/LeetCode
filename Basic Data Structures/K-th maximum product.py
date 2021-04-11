"""
Given two unsorted arrays A1 and A2 containing negative and positive integers of different lengths, find the kth maximum product of A1[i] * A2[j] ( a number from A1 * number from A2)

Example: A1=[7, -20, 3, 0, 10, -70] A2=[0, 1, -12, 100, -30] k=3

1st max = -70 * -30 = 2100
2nd max = 100 * 10 = 1000
k = 3rd max = -70 * -12 = 840 ( answer)
"""
import heapq
def k_th_max_product_brute_force(a, b, k):  # O(a*b*loga*logb) both
    """
    Just build a priority queue and return the k-th largest element
    """
    h = []
    for i in a:
        for j in b:
            h.append(-(i * j))
    heapq.heapify(h)
    for _ in range(k - 1):
        heapq.heappop(h)
    return -heapq.heappop(h)


def k_th_max_product_brute_force_optimized(a, b, k):  # O(a*b*logk*logk) and O(k)
    """
    Space optimization: 
    maintain a priority queue of size k 
    """
    h = []
    for i in a:
        for j in b:
            if len(h) < k:
                heapq.heappush(h, (i * j))
            else:
                heapq.heappushpop(h, (i * j))
    return heapq.heappop(h)


if __name__ == '__main__':
    print(k_th_max_product_brute_force([7, -20, 3, 0, 10, -70], [0, 1, -12, 100, -30], 3))
    print(k_th_max_product_brute_force_optimized([7, -20, 3, 0, 10, -70], [0, 1, -12, 100, -30], 3))