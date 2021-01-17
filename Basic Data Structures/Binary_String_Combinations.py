"""
Given a string s consisting of 0, 1 and ?. The question mark can be either 0 or 1. Find all possible combinations for the string.

Input: s = "001?"
Output: ["0010", "0011"]
"""

def binary_strings(s):
    res = []
    def _helper(s, curr_ix):
        if curr_ix == len(s):
            res.append(s)
            return
        if curr_ix < len(s) and s[curr_ix] == '?':
            _helper(s[:curr_ix] + '0' + s[curr_ix + 1:], curr_ix + 1)
            _helper(s[:curr_ix] + '1' + s[curr_ix + 1:], curr_ix + 1)
        else:
            _helper(s, curr_ix + 1)
    _helper(s, 0)
    return res


if __name__ == '__main__':
    print(binary_strings('001?'))