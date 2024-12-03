"""
Input is 7 distinct letters and output all possible combinations of the letters based on the below condition.
Words should be at least four letters. One character will be mandatory. e.g. I/TWADLN is input, where I is mandatory.
Examples: WAIT: yes LIT: no, too short WANT: no, does not contain mandatory letter ITWA: Yes 
FISH: no, contains letters not in the set
Questions INITIAL Generate all possible words
"""
def generate_letter_permutations(s, mandatory_ch):
    """
    Generate all combinations of 3 letter words and store it in a set.
    Iterate through each word and add mandatory character at all possible positions
    """
    s = set()
    final_res = set()
    updated_s = s.replace(mandatory_ch, "")
    def _helper(s, prefix, res):
        if len(prefix) == 3:
            res.add(prefix)
            return
        for i in range(len(s)):
            _helper(s[i+1], prefix + s[i], res)

    _helper(updated_s, "", s)
    # helper filled out our set s, now let's process
    for word in s:
        for i in range(len(word)):
            with_mandatory_char = w[:i] + mandatory_ch + w[i:]
            if len(with_mandatory_char) == 4:
                final_res.add(with_mandatory_char)
    return final_res