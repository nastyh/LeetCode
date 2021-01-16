import heapq
def findKthLargest_heap(nums, k):  # O(nlogk) and log(k)
    """
    Optimal solution: don't grow the heap more than k elements
    Adding an element to a heap of size k takes logk. 
    We traverse through the whole list, so nlogk
    """
    h = []
    for num in nums:
        if len(h) < k:
            heapq.heappush(h, num)
        else:
            heapq.heappushpop(h, num)
    return heapq.heappop(h)


def findKthLargest_brute_force_heap(nums, k):  # O(nlogn) and O(logn)
    """
    Put everything into the heap.
    Take out len(nums) - k elements
    The next one will be the one we need 
    """
    h = []
    for num in nums:
        heapq.heappush(h, num)
    for _ in range(len(nums) - k):
        heapq.heappop(h)
    return heapq.heappop(h)


def findKthLargest_sorting(nums, k):
    nums.sort()
    return nums[-k]


def findKthLargest_quick_sort(nums, k):  # quick sort is called log(N) times. Each time to sort N/(2^m) items. Space is O(N)
    # Partition function for quick sort
    # returns the final position of "Pivot" in a descending array
    def partition (nums, start, end):
        pivot = start
        while True:
            # if the current value is smaller than pivot, it is in the correct side
            # we can move left to the next element, we have to also check we are not passing
            # the left hand side pointer, start, which means all the elements are in the correct side.
            while start < end and nums[end] <= nums[pivot]:
                end -= 1
            # do the opposite thing to the left hand side pointer, start    
            while start < end and nums[start] >= nums[pivot]:
                start += 1 
            # if both left and right hand side have elements out of order,
            # we replace them
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
            # otherwise, we say all the elements are in the correct side except for the pivot
            # we will break the loop, and put the pivot to the correct position (exchange with right pointer). 
            else:
                break
        nums[end], nums[pivot] = nums[pivot], nums[end]
        return end

    def quicksort(nums, start, end):
            p = partition(nums, start, end)
            if p == k - 1: 
                return nums[p]
            elif p < k - 1:
                return quicksort(nums, p + 1, end)
            else:
                return quicksort(nums,start, p - 1)     

    return  quicksort(nums, 0 ,len(nums) - 1)


if __name__ == '__main__':
    print(findKthLargest_heap([3, 2, 1, 5, 6, 4], 2))
    print(findKthLargest_brute_force_heap([3, 2, 1, 5, 6, 4], 2))
    print(findKthLargest_sorting([3, 2, 1, 5, 6, 4], 2))
    print(findKthLargest_quick_sort([3, 2, 1, 5, 6, 4], 2))