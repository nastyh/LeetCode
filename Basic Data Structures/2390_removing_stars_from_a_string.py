class Solution:
    def removeStars(self, s: str) -> str:
        """
        O(n) both
        add to the stack
        if *, pop, otherwise append
        construct the res
        """
        st, res = [], ''
        if len(s) == 1:
            if s[0] != '*':
                return s
            else:
                return ''
        for ch in s:
            if len(st) == 0:
                st.append(ch)
            else:
                if ch == '*':
                    st.pop()
                else:
                    st.append(ch)
        return res.join(ch for ch in st)