class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = []
        for el in S:
            if not st:
                st.append(el)
                continue
            if st[-1] == el:
                st.pop()
            else:
                st.append(el)
        return ''.join(b for b in st)
