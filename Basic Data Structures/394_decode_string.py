class Solution:
    def decodeString(self, s: str) -> str:
        # need to multiply everything after the number
        # by this number
        # we need to go from the inside and to the sides
        stack = [] #  keep track of the current number and string that are being processed
        curr_str = ""  # store the current string that is being decoded
        curr_num = 0  #  current number that is being processed
        for c in s:
            # If the character is a digit, update the current number
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            # If the character is an opening bracket, push the current number and current string onto the stack
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                # Reset the current number and current string
                curr_num = 0
                curr_str = ""
            # If the character is a closing bracket, repeat the popped characters and push the result back onto the stack
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            # If the character is a letter, append it to the current string
            else:
                curr_str += c
        while stack:
            curr_str = stack.pop() + curr_str
        
        return curr_str

    def decodeString_another(self, s: str) -> str:
        st, curr_str = [], ""
        for c in s:
            # put everything into a stack till the first closing
            if c != "]":
                st.append(c)
            else:
            # now we need to build a portion of the answer 
                curr_str = ""
                # keep taking out everything that is inside a sq bracket in the stack
                while st[-1] != "[":
                    # add to the current portion of the answer
                    curr_str += st.pop()
                st.pop() # once it's processed, get rid of the last input
                curr_mult = ""  # need to have numbers 
                while st and st[-1].isdigit():
                    curr_mult += st.pop()
                st.append(curr_str * int(curr_mult[::-1])) # since it's  in the opposite direction
        return ''.join([w[::-1] for w in st])
