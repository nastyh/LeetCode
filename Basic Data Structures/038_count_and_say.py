class Solution:
    def countAndSay_short(self, n: int) -> str:
        """
        O(2^n) 
        O(2^n) to store the final string 
        """
        def _helper1(our_str):
            res = []
            i = 0
            while i < len(our_str):
                count = 1
                # count how many times s[i] repeats
                while i + 1 < len(our_str) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                res.append(str(count))
                res.append(our_str[i])
                i += 1
            return "".join(res)
        s = "1"
        # apply n - 1 times 
        for _ in range(1, n):
            s = _helper1(s)
        return s
    
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

    def countAndSay_recursively(self, n: int) -> str:
        """
         O(2^n) both
        The code iterates through the prev_say string.
        It counts the consecutive occurrences of each character.
        When a different character is encountered, it appends the count and the character to
        the curr_say string and resets the count.
        After the loop, it appends the count of the last character and the character
        itself to the curr_say string.
        """
        if n == 1:
            return "1"

        prev_say = self.countAndSay(n - 1)
        curr_say = ""
        count = 1

        for i in range(1, len(prev_say)):
            if prev_say[i] == prev_say[i - 1]:
                count += 1
            else:
                curr_say += str(count) + prev_say[i - 1]
                count = 1

        curr_say += str(count) + prev_say[-1]
        return curr_say
    
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
            

