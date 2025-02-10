class Solution:
    def clearDigits(self, s: str) -> str:
        """
        O(n) to go over
        O(n) for the stack
        Stack approach
        iterate over the string
        
        """
        st = []
        for candidate in s:
            if candidate.isdigit():
                if st:
                    st.pop()
            else:
                st.append(candidate)
        return ''.join(st)



    
