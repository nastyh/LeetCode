def permute(nums):
    def pmt(lst):
        out = []
        if not lst:
            return [lst]
        for i in range(len(lst)):
            a = lst[i:i+1]
            out.extend(a + x for x in pmt(lst[:i]+lst[i+1:]))
        return out
    return pmt(nums)

def permute_alt(nums):
    # output = []
    # recursively generate all permutations
    def _helper(nums):
        if len(nums) == 1: return [nums]
        # divide
        first, remainder = nums[0], nums[1:]
        permutations = _helper(remainder)
        # conquer
        tmp = []
        for permutation in permutations:
            for i in range(len(permutation)+1):
                # try to insert 'first' at all possible indexes
                tmp.append(permutation[:i] + [first] + permutation[i:])
        return tmp
    return _helper(nums)

if __name__ == '__main__':
    print(permute([1,2,3]))
    print(permute_alt([1,2,3]))
