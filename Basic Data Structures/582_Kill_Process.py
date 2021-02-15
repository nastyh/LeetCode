from collections import defaultdict
def killProcess(pid, ppid, kill):  # O(n) both
    """
    create a dictionary where keys are parents and values are children
    Then make a helper function that takes a value, appends it to res and calls itself on the value's values
    """
    d = defaultdict(list)
    res = []
    for parent_ix in range(len(ppid)):
        d[ppid[parent_ix]].append(pid[parent_ix])
    def _helper(value):
        res.append(value)
        for candidate in d[value]:
            _helper(candidate)
    _helper(kill)
    return res