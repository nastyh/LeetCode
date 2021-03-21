from collections import Counter
def reorderedPowerOf2(N):
    def helper(um):
        char_arr = str(num)
        table = dict()
        for char in char_arr:
            if char not in table:
                table[char] = 1
            else:
                table[char] += 1
        return table
    
    num_tab = helper(N)
    i = 0
    while i < 64:
        if num_tab == helper(pow(2, i)):
            return True
        else:
            i += 1
    return False


def reorderedPowerOf2_counts(N):  # O(log^2(N)) N different candidate powers of 2 and ecach has O(logN) complexity. Space is O(logN)
    d = Counter(str(N))
    return any(d == collections.Counter(str(1 << b)) for b in range(31))


def reorderedPowerOf2_permutations(N):  # O((logN)! * logN) for each of (logN)! permutations we need to check if it's a power of 2 (logN). Space is O(logN)
    """
    Generate all candidates using the same approach as in permutations. 
    Then iterate over all candidates and check if any of them is a power of two
    """
    candidates = []
    l = len(str(N))
    def _helper(N, curr_res):
        if len(curr_res) == l:
            candidates.append(curr_res[:])
        for i in range(len(str(N))):
            if i == 0 and str(N)[i] == 0: continue
            _helper(str(N)[:i] + str(N)[i + 1:], curr_res + str(N)[i])
    _helper(N, '')
    return any(candidate[0] != '0' and bin(int("".join(candidate))).count('1') == 1 for candidate in candidates)
    
    # or we can check it differently using bits: 

    # for num in candidates:
    #     if num[0] == '0': continue

    #     if int(num) != 0 and (int(num) & (int(num) - 1) == 0):
    #         return True
    # return False


if __name__ == '__main__':
    print(reorderedPowerOf2_permutations('16'))
    print(reorderedPowerOf2_permutations('10'))
    print(reorderedPowerOf2_permutations('24'))
    print(reorderedPowerOf2_permutations('1'))
    print(reorderedPowerOf2_permutations('218'))
    print(reorderedPowerOf2_permutations('376276711'))
