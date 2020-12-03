import heapq
def sort_k_messed_array(arr, k):
    """
    Array is almost sorted but every element can be not more than k positions to the left or to the right
    from its correct position. Need to sort it properly.
    Start building a heap. Once it has k elements, pop the smallest and add to the result
    Time: O(n * log(k)); n elements go through the heap
    Space: O(k) for the heap. O(n) for the result. Overall, it's O(n)
    """
    n = len(arr)
    heap = []
    answer = []

    for i in range(n):
        heapq.heappush(heap, arr[i])
        if i > k:
            answer.append(heapq.heappop(heap))
    while heap:
        answer.append(heapq.heappop(heap))
    return answer