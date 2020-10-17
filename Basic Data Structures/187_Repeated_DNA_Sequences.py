from collections import defaultdict
def findRepeatedDnaSequences(s):
    if len(s) < 10: return []
    # set for sequence
    sequence = set()
    # set for sequence with repetition
    repeated = set()
    for i in range( len(s) - 9):
        # make current sequence for i to i+10
        cur_seq = s[i:i+10]
        if cur_seq in sequence:
            # check for repetition
            repeated.add( cur_seq )
        # add to sequence set
        sequence.add( cur_seq )
    return [ *repeated ]


def findRepeatedDnaSequences_dict(s):
    if len(s) < 10: return []
    d = defaultdict(int)
    for i in range(len(s) - 9):
        curr = s[i:i + 10]
        d[curr] += 1
    return [k for k, v in d.items() if v > 1]


if __name__ == '__main__':
    print(findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
    print(findRepeatedDnaSequences_dict('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))