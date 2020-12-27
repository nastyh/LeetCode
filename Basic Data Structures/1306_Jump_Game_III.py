def canReach_bfs(arr, start):  # O(n) and O(n)
    """
     iterate all the possible routes and check if there is one reaches zero.
     However, if we already checked one index, we do not need to check it again.
     We can mark the index as visited by make it negative.
    """
    n = len(arr)
    q = [start]
    while q:
        node = q.pop(0)
        # check if reach zero
        if arr[node] == 0:
            return True
        if arr[node] < 0:
            continue
        # check available next steps            
        for i in [node + arr[node], node - arr[node]]:
            if 0 <= i < n:
                q.append(i)
        # mark as visited
        arr[node] = -arr[node]
    return False


def canReach_dfs(arr, start):  # O(n) and O(n)
    """
    make the value negative to mark as visited.
    """
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = -arr[start]
            return self.canReach_dfs(arr, start + arr[start]) or self.canReach_dfs(arr, start - arr[start])
        return False
