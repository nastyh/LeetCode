def letterCasePermutation(S):
    res = []
    def _helper(S, curr_res, curr_ix):
        if len(curr_res) == len(S):
            res.append(curr_res)
            return
        if S[curr_ix].isalpha():
            _helper(S, curr_res + S[curr_ix].lower(), curr_ix + 1)
            _helper(S, curr_res + S[curr_ix].upper(), curr_ix + 1)
        else:
            _helper(S, curr_res + S[curr_ix], curr_ix + 1)
    _helper(S, '', 0)
    return res


if __name__ == '__main__':
    print(letterCasePermutation('a1b2'))
    