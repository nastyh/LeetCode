"""
Given sorted integer arrays of different sizes, merge them into one sorted array.
Example 1:

Input:
[[1, 3, 5, 7],
[2, 4, 6],
[0, 8, 9, 10, 11]]

Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Example 2:

Input: [[1, 2, 3], [1, 2]]
Output: [1, 1, 2, 2, 3]
"""

def merge_lists(nums):  # O(mn) both where mn is the total number of elements in the list of lists nums
    if not nums:
        return []
    def merge(a, b):
        c = []
        while a and b:
            if a[0] <= b[0]:
                c.append(a.pop(0))
            else:
                c.append(b.pop(0))
        while a:
            c.append(a.pop(0))
        while b:
            c.append(b.pop(0))
        return c
    while len(nums) != 1:
        a = nums.pop()
        b = nums.pop()
        nums.append(merge(a, b))
    return nums[0]


if __name__ == '__main__':
    print(merge_lists([[1, 2, 3], [1, 2]]))