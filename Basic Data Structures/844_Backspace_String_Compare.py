 def backspaceCompare(S, T):  # O(n) and O(n)
     """
     Use stacks
     Edge cases: when # is in the beginning of the string or when there is nothing else there
     Taken care of by checking len()
     """
    ls, lt = [], []
    for ch in S:
        if ch != "#":
            ls.append(ch)
        else:
            if len(ls) <= 1:
                ls = []
            else:
                ls.pop()
    
    for ch in T:
        if ch != "#":
            lt.append(ch)
        else:
            if len(lt) <= 1:
                lt = []
            else:
                lt.pop()
    return ls == lt
    

def backspaceCompare_reversed(S, T):  # O(n) and O(1) b/c reversed returns an iterator
    """
    iterate through the string in reverse, then we will know how many backspace characters we have seen
    and therefore whether the result includes our character.
    Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped
    If a character isn't skipped, it is part of the final answer.
    """
    def F(S):
        skip = 0
        for x in reversed(S):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                yield x
    return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))