"""
Given an integer n, print all binary numbers that have exactly this nany digits
Input: n = 3
Output: ['000', '001', '010', etc]
"""
def print_all_binary(n):
    res = []
    def _helper(n, curr_res, curr_ix):
        if len(curr_res) == n:
            res.append(curr_res)
        for i in range(curr_ix, n):
            _helper(n, curr_res + '0', i + 1)
            _helper(n, curr_res + '1', i + 1)
    _helper(n, '', 0)
    return res


if __name__ == '__main__':
    print(print_all_binary(3))
