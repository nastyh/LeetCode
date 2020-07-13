from collections import Counter
def containsDuplicate(nums): # with a dicionary
    if len(nums) <= 1: return False
    d = Counter(nums)
    return sum(d.values()) / len(d) != 1

def containsDuplicate_set(nums):
    if len(nums) <= 1: return False
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    print(containsDuplicate([1, 2, 3, 1]))
    print(containsDuplicate([1, 3]))
    print(containsDuplicate_set([1, 2, 3, 1]))
    print(containsDuplicate_set([1, 3]))