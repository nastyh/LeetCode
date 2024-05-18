class Solution:
    def removeDuplicates_other(self, s: str, k: int) -> str:
        # we need to have a stack in a shape ([letter], [number of times in a row])
        # once the number becomes k, we pop the whole thing
        # we end up with the list of elements and their frequencies that are < k
        # just build the answer 
        st = []
        for ix in range(len(s)):
            if len(st) == 0: # if the stack is empty
                st.append([s[ix], 1]) # just add
            else:
                if st[-1][0] != s[ix]: # if the current letter isn't the same as the last in the stack
                    st.append([s[ix], 1])
                else: # letter is the same
                    if st[-1][1] < k: # under k
                        st[-1][1] += 1
                        if st[-1][1] == k: # time to get rid of the letter
                            st.pop()
        # result looks as [letter, number of times] so just build an answer
        return ''.join(st[i][0] * st[i][1] for i in range(len(st)))
    
