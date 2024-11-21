import math
def increasingTriplet(nums):
    if len(nums) < 3: return False
    first, second = math.inf, math.inf
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False 


def increasingTriplet_brute_force(nums):  # O(n^2) and O(1)
    """
    Just recheck every three numbers using the helper function
    """
    res = []
    def _helper(arr):
        for j in range(1, len(arr)):
            if arr[j] <= arr[j - 1]:
                return False
        return True
    for i in range(2, len(nums)):
        if _helper(nums[i - 2: i + 1]):
            return True
    return False 

# not always working
def increasingTriplet_stack(nums):   # O(n) and O(n % 3) --> O(n)
    """
    Start with a stack, put the first element
    Start iterating. If a current element is larger than the last element in the stack, then append.
    If a current element <= than the last element in the stack, clean the stack
    If at any point stack has three elements, return True
    Otherwise run till the end and return False 
    """
    if len(nums) < 3: return False
    if len(set(nums)) == 1: return False
    st = []
    st.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i] > st[-1]:
            st.append(nums[i])
        else:
            for _ in range(len(st)):
                st.pop()
            st.append(nums[i])
        if len(st) == 3:
            return True
    return False

if __name__ == '__main__':
    print(increasingTriplet([1, 2, 3, 4, 5]))
    print(increasingTriplet([5, 1, 5, 5, 2, 5, 4]))  # THAT SHOULD BE FALSE
    print(increasingTriplet([5, 4, 3, 2, 1]))
    print(increasingTriplet([2, 1, 5, 0, 4, 6]))
    print(increasingTriplet_brute_force([1, 2, 3, 4, 5]))
    print(increasingTriplet_brute_force([5, 1, 5, 5, 2, 5, 4]))
    print(increasingTriplet_brute_force([5, 4, 3, 2, 1]))
    print(increasingTriplet_brute_force([2, 1, 5, 0, 4, 6]))
    print(increasingTriplet_stack([1, 2, 3, 4, 5]))
    print(increasingTriplet_stack([5, 1, 5, 5, 2, 5, 4]))
    print(increasingTriplet_stack([5, 4, 3, 2, 1]))
    print(increasingTriplet_stack([2, 1, 5, 0, 4, 6]))
