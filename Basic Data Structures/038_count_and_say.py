class Solution:
    def countAndSay_helper(self, n: int) -> str:
        """
        st to build a structure 
        O(4^n/3) both 
        """
        if n == '1': return '1' # edge case 
        def _helper(s_input): 
            res = []
            st = []
            for s in s_input:
                if st and s != st[-1]:
                    prev = st[-1]
                    curr_count = 0 
                    while st and st[-1] == prev:
                        """
                        if something is in the stack and it's the same element
                        take them out, increment the curr_count of this element 
                        """
                        st.pop()
                        curr_count += 1 
                    res.append(str(curr_count))
                    res.append(prev)
                    st.append(s)
                else:
                    st.append(s)
            if st:
                res.append(str(len(st)))
                res.append(st[-1])
            return ''.join(x for x in res)
        
        curr = '1'
        for i in range(2, n + 1):
            curr = _helper(curr)
        return curr

    def countAndSay_no_helper(self, n: int) -> str:
        """
        Same but in one place 
        build helper string s2 and use curr_element as the last stack's element 
        """
        s1, s2 = '1', ''
        for _ in range(2, n + 1):
            curr_count = 0
            curr_element = s1[0]
            for ch in s1:
                if ch == curr_element:
                    curr_count += 1 
                else:
                    s2 += str(curr_count) + curr_element 
                    curr_count = 1
                    curr_element = ch 
            s2 += str(curr_count) + curr_element 
            s1 = s2 
            s2 = ''
        return s1
            

