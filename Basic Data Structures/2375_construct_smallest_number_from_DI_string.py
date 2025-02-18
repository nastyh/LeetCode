class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        O(n) both
        iterate over the pattern and push numbers onto the stack.
        When we encounter an 'I' or reach the end, we pop from the stack to build our result.
        This ensures that when we have a sequence of 'D's, we push the numbers first and then
        pop them in reverse order (producing the decreasing order), and when we hit an 'I',
        we flush the stack which results in an increasing sequence.
        """
        st, res = [], ""
        for i in range(len(pattern)+1):
            st.append(str(i+1))
            if i == len(pattern) or pattern[i] == 'I':
                while st:
                    res+= st.pop()
        return res