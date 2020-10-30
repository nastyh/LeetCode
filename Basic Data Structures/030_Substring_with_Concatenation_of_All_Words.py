def findSubstring(s, words):
    w_dict = dict()
    answer = list()
    for word in set(words):
        id = -1
        while True:
            try:
                id = s.index(word, id+1)
                w_dict[id] = word
            except:
                break
    for k, v in w_dict.items():
        w_copy = words[:]
        start = k
        w_copy.remove(v)
        i = k + len(v)
        while w_copy:
            try:
                w = w_dict[i]
                w_copy.remove(w)
                i += len(w)
            except:
                break
        if w_copy == []:
            answer.append(k)
    return answer


def findSubstring_alt(s, words):
    """
     The first dict allwords stores all the word in words as key and accumulates their respective required counts as value.
     Then, for each starting position i in string s, we refer to another dict thissegmentwords, which store the word:count pair in the s[i:i+lenallwords].
     At each step, we check the substring s[i:i+lenoneword] and then increases i by lenoneword. During the scanning, if the substring your are checking is not
     presented in the first dict allwords or if its count is larger than its required count (thissegmentwords[temp_word] > allwords[temp_word]), then you can
     directly break and go check the next position i. Else, you can keep scanning. If at the end of the first loop, you find out that the two dicts are identical,
     then this current substring s[i:i+lenallwords] is a legit substring so you save the index i.
    """
    if not s or not words:
        return []
    
    allwords = {}
    for word in words:
        if word in allwords:
            allwords[word] += 1
        else:
            allwords[word] = 1
    
    lens = len(s)
    lenoneword = len(words[0])
    lenallwords = len(words) * lenoneword
    ans = []
    
    for i in range(lens - lenallwords + 1):
        thissegmentwords = {}
        for start in range(i, i + lenallwords, lenoneword): 
            temp_word = s[start: start + lenoneword]       
            if temp_word in allwords:
                if temp_word in thissegmentwords:
                    thissegmentwords[temp_word] += 1
                    if thissegmentwords[temp_word] > allwords[temp_word]:
                        break
                else:
                    thissegmentwords[temp_word] = 1
            else:
                break
        if allwords == thissegmentwords:
            ans.append(i)
    return ans

