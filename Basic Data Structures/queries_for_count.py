"""
The task is to determine the number of elements within a specified range in an unsorted array.
Given an array of size n, the goal is to count the elements that fall between two given values, i and j, inclusively.
"""
def count_elements_in_range_search(arr, ranges):
    """
    O(nlogn + rlogn), r ranges
    O(r), r num of range queries 
    """
    # Sort the array
    arr.sort()
    results = []

    def _left_helper(arr, x):
        """
        Find the leftmost index where x can be inserted to maintain sorted order
        """
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left

    def _right_helper(arr, x):
            """
            Find the rightmost index where x can be inserted to maintain sorted order
            """
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] <= x:
                    left = mid + 1
                else:
                    right = mid
            return left
    for i, j in ranges:
        # Use custom bisect functions
        left_index = _left_helper(arr, i)
        right_index = _right_helper(arr, j)
        count = right_index - left_index
        results.append(count)
    return results

def count_elements_in_range_bruteforce(arr, ranges):
    """
    O(nr)
    O(r)
    """
    results = []
    for i, j in ranges:
        count = sum(1 for x in arr if i <= x <= j)
        results.append(count)
    return results