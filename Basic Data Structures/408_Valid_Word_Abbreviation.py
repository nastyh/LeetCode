def validWordAbbreviation(word, abbr):
    i = j = 0 
    while j < len(abbr) and i < len(word): 
        if abbr[j].isalpha(): 
            if abbr[j] != word[i]: 
                return False 
            i += 1 
            j += 1 
        else: 
            if abbr[j] == '0':  # to handle edge cases such as "01", which are invalid
                return False 
            temp = 0 
            while j < len(abbr) and abbr[j].isdigit(): 
                temp = temp * 10 + int(abbr[j]) 
                j += 1 
            i += temp  
    return j == len(abbr) and i == len(word)
    
def validWordAbbreviation_another(word, abbr):
    orig_pos = 0 # index at the original position
    i = 0 # to iterate over an observation
    while i < len(abbr):
        # invalid cases
        if abbr[i] == '0' or orig_pos >= len(word):
            return False
        num = ''
        # processing numbers
        while i < len(abbr) and abbr[i].isdigit():
            num += abbr[i]
            i += 1
        if num:
            orig_pos += int(num)
        else:
            if abbr[i]!= word[orig_pos]:
                return False
            orig_pos += 1
            i += 1
    return orig_pos == len(word)
