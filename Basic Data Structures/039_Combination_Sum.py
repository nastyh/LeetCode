def combinationSum(candidates, target): # returns a list of list
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

