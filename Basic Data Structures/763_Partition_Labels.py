def partitionLabels(S):
    """
    create a dict with keys being characters and values being the last indices of these characters in a string
    loop through the string
    If we are at an index that shows that we won't see this character again, then we found a partition for this letter
    Add results to res, switch to the next character
    It's a greedy approach overall
    """
    if len(S) == 1: return [1]
    d = {}
    st, end, res = 0, 0, []
    for k, v in enumerate(S):
        d[v] = k
    for ix in range(len(S)):
        end = max(end, d[S[ix]])
        if ix == end:
            res.append(end - st + 1)
            st = end + 1
    return res