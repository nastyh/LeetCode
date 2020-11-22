def countSmaller_naive(nums):  # O(n^2). Times out but works
    if len(nums) == 0: return []
    if len(nums) == 1: return [0]
    if len(nums) == 2:
        if nums[-1] < nums[0]:
            return [1, 0]
        else:
            return [0, 0]
    res = [0] * len(nums)
    for i in range(len(nums) - 1):
        curr = 0
        for n in range(i + 1, len(nums)):
            if nums[n] < nums[i]:
                curr += 1
        res[i] = curr
    return res

def countSmaller_binary(nums):
    n = len(nums)
    if not n:
        return []
    # Create a sorted list with last element of given arr
    sorted_list = [nums[-1]]
    # Last number has 0 smaller elements to its right
    output = [0]

    def search(arr, target):
        na = len(arr)
        left, right = 0, na - 1

        # Quick checks of sorted list beg and end index values
        if arr[0] >= target:
            return 0
        if arr[-1] < target:
            return na

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                # If you have found the number, great!
                # but you want the number smaller to it
                # Linear probe backwards from mid, unless
                # you find different number (since sorted)
                # you will find the next smaller number and
                # return its index
                while mid > 0 and arr[mid] == target:
                    mid -= 1
                return mid + 1
            
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # Since we have already processed last element, start from n - 2
    for i in range(n - 2, -1, -1):
        # Binary search the index
        index = search(sorted_list, nums[i])
        output.append(index)
        # Grow the sorted list after every iteration
        # By inserting the element in correct index position
        sorted_list.insert(index, nums[i])

    return output[::-1]


if __name__ == '__main__':
    print(countSmaller_naive([5, 2, 6, 1]))
    print(countSmaller_binary([5, 2, 6, 1]))