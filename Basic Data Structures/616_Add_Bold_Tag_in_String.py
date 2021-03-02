def addBoldTag(s, dict):  # O(n) both 
    if not s: return ""
        if not dic: return s
        # find ranges
        ranges = []
        word_lens = list(map(len,dic))
        min_word_len, max_word_len = min(word_lens), max(word_lens)
        dic = set(dic)
        for i, ch in enumerate(s):
            for j in range(i + min_word_len, min(len(s),i + max_word_len) + 1):
                if s[i:j] in dic:
                    ranges.append((i,j-1))                     
        # merge ranges
        ranges.sort(key = lambda x:(x[0], -x[1]))
        st = []
        for x, y in ranges:
            if st and st[-1][1] >= x - 1:
                st[-1] = [st[-1][0], max(y, st[-1][1])]
            else:
                st.append([x, y])
        # mark <b>
        starts, ends = set(x for x,_ in st), set(y for _,y in st)
        ans = ""
        for i, ch in enumerate(s):
            if i in starts:
                ans += "<b>" + ch
                if i in ends:
                    ans += "</b>"
            elif i in ends:
                ans += ch + "</b>"
            else:
                ans += ch
        return ans

class Trie(object):
    def __init__(self):
        self.data = {}
        
    def addWord(self,word):
        temp = self.data
        for i,c in enumerate(word):
            if c not in temp:
                break
            temp = temp[c]
        else:
            i+=1
        
        for j in word[i:]:
            temp[j]={}
            temp = temp[j]
        temp['#']={}
    
    def search(self,string,index):
        """
        search largest string
        """
        rem =- 1
        temp = self.data
        for i in range(index, len(string)):
            if string[i] not in temp:
                return rem
            if '#' in temp[string[i]]:
                rem = i
            temp = temp[string[i]]
        if '#' in temp:
            return len(string) - 1
        return rem

    def addBoldTag_trie(s, dict):
        if not wordlist or not s:
            return s
        trie = Trie()
        for word in wordlist:
            trie.addWord(word)
        
        res = []
        i=0
        while i<len(s):
            end = trie.search(s,i)
            if end !=- 1:
                if not res:
                    res.append([i,end])
                else:
                    if i <= res[-1][1] + 1:
                        #start of this is less than end of previous
                        res[-1][0] = min(res[-1][0], i)
                        res[-1][1] = max(res[-1][1], end)
                    else:
                        res.append([i,end])
            i += 1
        if not res:
            return s
        final = ""
        prevEnd = 0
        for start,end in res:
            if start > prevEnd:
                final += s[prevEnd:start]
            final = final + "<b>" + s[start:end + 1] + "</b>"
            prevEnd = end + 1
        if prevEnd!=len(s):
            final += s[prevEnd:]
        return "".join(final)
