def numRescueBoats(people, limit):
    """
    Sorting allows to save the lightest and the heaviest 
    If their weights <= limit, save both, move the pointers, increment res
    Otherwise, move the right one, since it's too heavy 
    """
    people.sort()
    l, r = 0, len(people) - 1
    res = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
            r += 1
         else: r -= 1
         res += 1
    return res
