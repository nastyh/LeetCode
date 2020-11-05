def minCostToMoveChips(position):
    evens, odds = 0, 0 
    for n in position:
        if n % 2 == 0:
            evens += 1
        else:
            odds += 1
    return min(evens, odds)