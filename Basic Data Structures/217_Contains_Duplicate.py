from collections import Counter
def containsDuplicate(nums): # with a dicionary
    if len(nums) <= 1: return False
    d = Counter(nums)
    return sum(d.values()) / len(d) != 1


def containsDuplicate_another(nums):
    d = Counter(nums)
    return sum(d.values()) != len(d)


def containsDuplicate_set(nums):
    if len(nums) <= 1: return False
    return len(nums) != len(set(nums))
    

def containsDuplicate_sort(nums):
    nums.sort()
    for el_ix in range(len(nums) - 1):
        if nums[el_ix] == nums[el_ix + 1]:
            return True
    return False


if __name__ == '__main__':
    print(containsDuplicate([1, 2, 3, 1]))
    print(containsDuplicate([1, 3]))
    print(containsDuplicate_set([1, 2, 3, 1]))
    print(containsDuplicate_set([1, 3]))
    print(containsDuplicate_another([1, 3]))
    print(containsDuplicate_sort([1, 3]))
    print(containsDuplicate_sort([1, 2, 3, 1]))