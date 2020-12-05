from collections import Counter
def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)


def canBeEqual_dict(target, arr):
    return Counter(target) == Counter(arr)