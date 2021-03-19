from collections import Counter
def majorityElement(nums): # O(n) both
    d = Counter(nums)
    for k, v in d.items():
        if v > len(nums) // 2:
            return k


def majorityElement_sort(nums):  # O(nlogn) and O(1)
    """
    in a sorted array a majority element will always be at the middle index
    """
    nums.sort()
    return nums[len(nums) // 2]


def majorityElement_Boyer_Moore(nums):  # O(n) and O(1)
    """
    Look for a suffix sufsuf of nums where suf[0]suf[0] is the majority element in that suffix.
    To do this, we maintain a count, which is incremented whenever we see an instance of our current candidate for majority element and decremented
    whenever we see anything else.
    Whenever count equals 0, we effectively forget about everything in nums up to the current index and consider the current number as the candidate
    for majority element. 
    """
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
