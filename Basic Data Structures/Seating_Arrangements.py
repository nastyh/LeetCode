"""
There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table.
As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights.
Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible
overall awkwardness of any seating arrangement.

n = 4
arr = [5, 10, 6, 8]
output = 4
If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table (having heights [6, 5, 8, 10], in that order),
then the four awkwardnesses between pairs of adjacent guests will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4, yielding an overall awkwardness of 4.
It's impossible to achieve a smaller overall awkwardness.
"""

def minOverallAwkwardness(arr):  # O(nlogn) and O(1)
    arr.sort()
    arr = arr[::2] + list(reversed(arr[1::2]))
    m = abs(arr[-1] - arr[0])
    for i in range(1, len(arr)):
        m = max(m, abs(arr[i] - arr[i - 1]))
    return m


def minOverallAwkwardness_another(arr):  # O(nlogn) and O(1)
    """
        sort the array
    iterate on sorted array and append one time to the right and next time to the left of the result to get minimum in max distance
    """
    max_dist = 0
    arr.sort()
    for i in range(len(arr)):
        if i == 0:
            right = left = arr[0]
            continue
        if i % 2 == 0:
        max_dist = max(max_dist, arr[i] - right)
        right = arr[i]
        else:
        max_dist = max(max_dist, arr[i] - left)
        left = arr[i]
    return max_dist