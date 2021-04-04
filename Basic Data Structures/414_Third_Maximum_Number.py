import heapq
def thirdMax(nums):  #O(nlogn) and O(n) in the worst case
    """
    Straightforward: add unique elements to the heap.
    Then pop elements either 3 times or, if the number of elements is < 3, then all but the last one
    Pop one more time returning the result
    """
    seen = set()
    h = []
    for num in nums:
        if -num not in seen:
            heapq.heappush(h, -num)
            seen.add(-num)
    if len(seen) < 3:
        return max(nums)
    for _ in range(min(len(h) - 1, 2)):
        -heapq.heappop(h)
    return -heapq.heappop(h)


def thirdMax_heap_3(nums):  # O(nlog3) and O(n)
    """
    Maintain a heap with three smallest elements
    If the heap's size < 3, then just add an element
    Otherwise, add an element and pop. The order is important. This is how heappushpop works 
    """
    h = []
    for x in set(nums):
        if len(S) < 3:
            heapq.heappush(h, x)
        else:
            heapq.heappush(h, x)
            heapq.heappop(h)
            # heapq.heappushpop(h, x)  # alternative one-liner
        return h[0] if len(h) == 3 else max(h)


def thirdMax_set(nums):  #O(n) and O(1)
    """
    Overwrite nums to achieve O(1) space
    Then just remove two largest values and return the next largest 
    """
    nums = set(nums)
    if len(nums) < 3:
        return max(nums)
    nums.remove(max(nums))
    nums.remove(max(nums))
    return max(set(nums))


def thirdMax_math(nums):  # O(n) both 
    if len(set(nums)) < 3: return max(nums)
    first = second = third = float('-inf')
    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third  and num != first and num != second:
            third = num
    return third