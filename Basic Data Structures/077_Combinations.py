def combine(self, n: int, k: int) -> List[List[int]]:
    """
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
    n = 4, k = 2
    [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    backtracking
    curr represents the current answer we're building
    add the first element (1) and find all combinations that start with 1
    we start by adding the first element after 1, which is 2. We now have curr = [1, 2].
    We are locking in this 2 and we will now find all combinations that start with 1, 2.
    we have finished finding all combinations that start with [1, 2].
    We backtrack by removing the 2, and we have curr = [1] again.
    Now, we add the second element that comes after 1, which is 3. We have curr = [1, 3],
    and now we need to find all combinations that start with [1, 3].
    O(n! / (k - 1)! * (n - k)!) -- it's essentially k picks of n, combinatorial formula
    O(k) -- for the recursion stack
    """
    res = []
    def _helper(curr_res, first_num):
        if len(curr_res) == k:
            res.append(curr_res[:])
            return
        need = k - len(curr_res)
        remains = n - first_num + 1
        available = remains - need
        for num in range(first_num, first_num + available + 1):
            curr_res.append(num)
            _helper(curr_res, num + 1)
            curr_res.pop()
        
    _helper([], 1)
    return res

def combine_list(self, n: int, k: int) -> List[List[int]]:
    """
    O(n! / (k - 1)! * (n - k)!) 
    O(n + k) -- probably is O(n)
    """
    nums = [i for i in range(1, n + 1)]
    res = []
    def _helper(nums, curr_ix, curr_res):
        if len(curr_res) == k:  # edge case, result is ready
            res.append(curr_res)
        for i in range(curr_ix, len(nums)):
            _helper(nums, i + 1, curr_res + [nums[i]]) # move to the next index, attach what we've built so far
    _helper(nums, 0, [])
    return res


def combine(n, k):  # O(k*CkchooseN) and O(CkchooseN)
    nums = [i for i in range(1, n + 1)]
    res = []
    def _helper(nums, curr_ix, curr_res):
        if len(curr_res) == k:
            res.append(curr_res)
        for i in range(curr_ix, len(nums)):
            # curr_res.append(nums[i])
            _helper(nums, i + 1, curr_res + [nums[i]])
    _helper(nums, 0, [])
    return res


def combine_alt(n, k):
    result = []
    nums = [i for i in range(1,n + 1)]
    def backtrack(start, end, tmp):
        if len(tmp) == k:
            result.append(tmp[:])
        else:
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i + 1, end, tmp)
                tmp.pop()
    backtrack(0, n, [])
    return result


if __name__ == '__main__':
    print(combine(4, 2))
    print(combine_alt(4, 2))
