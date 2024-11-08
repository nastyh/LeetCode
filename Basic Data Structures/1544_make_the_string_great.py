class Solution:
    def makeGood(self, s: str) -> str:
        """
        O(n) both
        Add letters to the stack: if it's empty, add
        If the last is the same as the current, add
        If the last lowered == current or the last == current lowered, pop
        Will be left with the good letters --> construct the resulting string 
        """
        if len(s) == 1: return s
        st = []
        for el in s:
            if len(st) == 0:
                st.append(el)
            else:
                if st[-1] == el: st.append(el)
                elif st[-1].lower() == el or st[-1] == el.lower():
                    st.pop()
                else: st.append(el)
        res = ''
        return ''.join(letter for letter in st)