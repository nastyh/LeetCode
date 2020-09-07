from collections import Counter
def findSpecialInteger(arr):  # brute force solution without using the fact that the list is in a non-decreasing order
    threshold = len(arr) // 4
    d = Counter(arr)
    return [k for k, v in d.items() if v > threshold][0]


def findSpecialInteger_fast(arr):
    if len(arr) == 1: return arr[0]
    threshold = len(arr) // 4
    curr_res = 1
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == prev:
            curr_res += 1
            if curr_res > threshold:
                return arr[i]
        else:
            curr_res = 1
            prev = arr[i]


if __name__ == '__main__':
    print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))
    print(findSpecialInteger_fast([1,2,2,6,6,6,6,7,10]))