"""
Use topological sort to compute transitive closures of the courses' prerequisites and store them in the form of prerequisite bitmasks:
 ith bit means whether course i must be taken before.
Solve the problem by top-down bitmask DP, where ith bit of the state bitmask indicates whether course i has been taken.
Read out the available courses that are not taken yet by comparing the state bitmask with the precomputed prerequisite bitmasks (masks[i] & mask == masks[i]).
If the number of available courses <= k, take all of them. Otherwise, use itertools.combinations(avail, k) to iterate through all the possible combinations.
Return 0 for the base case dp(2 ** n - 1)
Time complexity: O(2 ^ n * C(n, k) * n) since there are 2 ^ n possible states, and for each state the upper bound of the time complexity is C(n, k) * n 
where C is the binomial coefficient
"""
def minNumberOfSemesters(n, dependencies, k):
    backward = {i: set() for i in range(n)}
    forward = {i: set() for i in range(n)}
    avail = set(range(n))
    for pre, post in dependencies:
        pre -= 1
        post -= 1
        backward[post].add(pre)
        forward[pre].add(post)
        avail.discard(post)
    masks = [0] * n
    while avail:
        new_avail = set()
        for i in avail:
            for f in forward[i]:
                masks[f] |= masks[i]
                masks[f] |= 2 ** i
                backward[f].remove(i)
                if not backward[f]:
                    new_avail.add(f)
        avail = new_avail

    @functools.lru_cache(None)
    def dp(mask):
        if mask == 2 ** n - 1:
            return 0
        avail = {i for i in range(n) if (not 2 ** i & mask) and masks[i] & mask == masks[i]}
        if len(avail) <= k:
            for i in avail:
                mask |= 2 ** i
            return 1 + dp(mask)
        ans = math.inf
        for comb in itertools.combinations(avail, k):
            diff = sum(2 ** i for i in comb)
            ans = min(ans, 1 + dp(mask | diff))
        return ans
        
    return dp(0)