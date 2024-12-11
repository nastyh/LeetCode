"""
Input is 7 distinct letters and output all possible combinations of the letters based on the below condition.
Words should be at least four letters. One character will be mandatory. e.g. I/TWADLN is input, where I is mandatory.
Examples: WAIT: yes LIT: no, too short WANT: no, does not contain mandatory letter ITWA: Yes FISH: no, contains letters not in the setQuestions INITIAL Generate all possible words
"""
def generate_words(letters, mandatory_letter):
    def _helper(letters, curr_word, words, mandatory_letter):
        if len(curr_word) >= 4 and mandatory_letter in curr_word:
            words.append(curr_word)
        for i in range(len(letters)):
            new_word = curr_word + letters[i]
            new_letters = letters[:i] + letter[i+1:]
            _helper(new_letters, new_word, words, mandatory_letter)

    words = []
    _helper(letters, "", words, mandatory_letter)
    return words
