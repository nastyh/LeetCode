def maximumUnits(boxTypes, truckSize):  # O(nlogn) and O(1)
    """
    Sort by the maximum units per box
    Start taking boxes greedily.
    Every time you can take the min of the current capacity and however many boxes are at your disposal 
    Update how much capacity is left after it 
    """
    boxTypes.sort(key = lambda x: x[1], reverse = True)
    res = 0 
    for element in boxTypes:
        if truckSize != 0:
            new_portion = min(element[0], truckSize) * element[1]
            res += new_portion
            truckSize -= min(element[0], truckSize) 
        else:
            break
    return res 


if __name__ == '__main__':
    print(maximumUnits([[1, 3], [2, 2], [3, 1]], 4))
    print(maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
    print(maximumUnits([[1, 3], [5, 5], [2, 5], [4, 2], [4, 1], [3, 1], [2, 2], [1, 3], [2, 5], [3, 2]], 35))
