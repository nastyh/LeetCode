def longestCommonPrefix(strs):
    if not strs:
        return ''
    strs.sort()
    if strs[0]:
        for i, (u, v) in enumerate(zip(strs[0], strs[-1])):
            if u != v:
                return strs[0][:i]
    return strs[0]

# easier to comprehend

def longestCommonPrefix_alt(strs):
    if len(strs) == 0: return ''
    zipped = zip(*strs)
    prefix_ix = 0
    for ch in zipped:
        unique = set(ch)
        if len(unique) != 1: break
        else:
            prefix_ix += 1
    return strs[0][:prefix_ix]


def longestCommonPrefix_sorting(strs):  # O(nlogn) and O(1)
    """
    Longest will be the last after sorting
    """
    if len(strs) == 0:
        return '' 
    res = ''
    strs = sorted(strs)
    for i in strs[0]:
        if strs[-1].startswith(res + i):
            res += i
        else:
            break
    return res


class Trie:  # O(S) preprocessing wher S is the number of all chars in the array. Trie build O(S), space O(S)
        self.end_of_word = False
        self.children = {}
        
    def insert(self, word):
        curr = self
        idx = 0
        while(idx < len(word)):
            if(word[idx] not in curr.children):
                curr.children[word[idx]] = Trie()
            curr = curr.children[word[idx]]
            idx += 1
        curr.end_of_word = True

    def getLongest(self):
        curr = self
        res = ""
        while(len(curr.children) == 1):
            if(curr.end_of_word):
                break
            val = list(curr.children.keys())
            res += val[0]
            curr = curr.children[val[0]]
        return res


def longestCommonPrefix_trie(strs):
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    t = Trie()
    for word in strs:
        t.insert(word)
    return t.getLongest()


if __name__ == '__main__':
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix_alt(["flower","flow","flight"]))
