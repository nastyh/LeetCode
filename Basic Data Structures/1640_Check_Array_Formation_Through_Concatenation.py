def canFormArray(arr, pieces):  # O(n^2) and O(1)
    n = len(arr)
    i = 0
    while i < n:
        # find target piece
        for p in pieces:
            if p[0] == arr[i]:
                break
        else:
            return False
        # check target piece
        # python saves the last iterated `p`
        for x in p:
            if x != arr[i]:
                return False
            i += 1
    return True

def canFormArray_bin_search(arr, pieces):  # O(nlogn) and O(1)
    n = len(arr)
    p_len = len(pieces)
    pieces.sort()
    i = 0
    while i < n:
        left = 0
        right = p_len - 1
        found = -1
        # use binary search to find target piece:
        while left <= right:
            mid = (left + right)//2
            if pieces[mid][0] == arr[i]:
                found = mid
                break
            elif pieces[mid][0] > arr[i]:
                right = mid - 1
            else:
                left = mid + 1
        if found == -1:
            return False
        # check target piece
        target_piece = pieces[found]
        for x in target_piece:
            if x != arr[i]:
                return False
            i += 1
    return True


def canFormArray_dict(arr, pieces):  # O(n) and O(n)
    n = len(arr)
    # initialize hashmap
    mapping = {p[0]: p for p in pieces}
    i = 0
    while i < n:
        # find target piece
        if arr[i] not in mapping:
            return False
        # check target piece
        target_piece = mapping[arr[i]]
        for x in target_piece:
            if x != arr[i]:
                return False
            i += 1
    return True


def canFormArray_another_dict(arr, pieces): # O(n) and O(n)
    mapping = {}
    for piece in pieces:
        mapping[piece[0]] = piece
    ans = []
    for num in arr:
        if num in mapping:
            ans += mapping[num]
    return ans == arr


if __name__ == '__main__':
    print(canFormArray([49, 18, 16], [[16, 18, 49]]))