def findCelebrity(n):  # O(n) both
    """
    Eliminate people down to a single candidate and then check whether it's a celebrity using the respective function
    """
    def isCelebrity(i):
        for j in range(n):
            if i != j and knows(i, j) or not knows(j, i):
                return False
        return True
    candidate = 0    
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    if isCelebrity(candidate):
        return candidate
    return -1 


def findCelebrity_other(n):  # O(n) both
    isCelebrity = [True] * n
    for i in range(n):
        if isCelebrity[i]:
            for j in range(n):
                if j != i and (knows(i, j) or not knows(j, i)):
                    isCelebrity[i] = False
                    break
            if isCelebrity[i]:
                return i
    return -1