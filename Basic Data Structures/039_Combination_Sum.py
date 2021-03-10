def combinationSum(candidates, target): # returns a list of list O(M^2 * N) and O(M^2) where M is target and N == len(candidates)
    """
    Define dp(i) as all unique combinations whose sum is i.
    We'll get the recursion below for the number candiates[j]:
    dp(i) += [candidates[j]] if i == candidates[j]
    dp(i) += [s + [c] for s in dp(i - candidates[j])] if i - candidates[j] > 0
    """
    dp = [[] for _ in range(target + 1)]
    for c in candidates:
        for i in range(1, target + 1):
            if i == c:
                dp[i].append([c])
            elif i - c > 0:
                dp[i] += [s + [c] for s in dp[i - c]]
    return dp[target]


def combinationSum_alt(candidates, target):
    def helper(candidates, target, _sum, start, path):
        result = []
        for i in range(start, len(candidates)):
            total = _sum + candidates[i]
            if total < target:
                result += helper(candidates, target, total, i, path + (candidates[i],))
            elif total == target:
                result.append(list(path + (candidates[i],)))
        return result
    return helper(candidates, target, 0, 0, ())


def combinationSum_best(candidates, target):  # O(N^(M/min_cand + 1)), O(M/min_cand), where N == len(candidates), M - target, min_cand == min(candidates_)
    """
    Idea: recursion. We take an element and see whether target - element == 0. If yes, it means
    we just found a good combination. Just add it to res.
    If target - element < 0, then we overshot. We don't need to build this combination further, call it a day.
    If target - element > 0: take the same element once again and repeat the whole thing.
    Tricky things: how to not include the same combinations and when finally move to the next element.
    It's taken care of in the "for" loop. It moves to another i only after a round of recursion for the curren i is completed.
    So we are sure that we've exhausted combinations when an element repeats. Example [2, 2, 2] to get to target 6.
    """
    res = []
    def _helper(candidates, target, curr_path, curr_ix):
        if target < 0: return 
        if target == 0:
            res.append(curr_path)
        for i in range(curr_ix, len(candidates)):
            _helper(candidates, target - candidates[i], [candidates[i]] + curr_path, i)
    _helper(candidates, target, [], 0)
    return res


if __name__ == '__main__':
    print(combinationSum_best([2, 3, 6, 7], 7))
    print(combinationSum_best([2, 3, 5], 8))