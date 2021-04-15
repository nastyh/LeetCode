def minSwaps(data):
    i, acc = 0, 0
    res, ones = float('inf'), sum(data)
    for j in range(len(data)):
        acc += data[j]
        # Have finally built a window of size number_of_ones
        if j - i + 1 == ones:
            res = min(res, j - i + 1 - acc)
            acc -= data[i]
            i += 1
    # If the input array has 0 ones, return 0. Otherwise return result.
    return res if res != float('inf') else 0


if __name__ == '__main__':
    print(minSwaps([1, 0, 1, 0, 1]))
    print(minSwaps([0, 0, 0, 1, 0]))
    print(minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))
    print(minSwaps([1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1]))
